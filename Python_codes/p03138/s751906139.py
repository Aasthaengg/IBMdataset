N,K=map(int,input().split())
A=list(map(int,input().split()))

data=[0 for i in range(45)]
for a in A:
    b=list(bin(a)[2:])
    b.reverse()
    for i in range(len(b)):
        if b[i]=="1":
            data[i]+=1
numlst=[]
bink=list(bin(K)[2:])
bink.reverse()
K_nagasa=len(bink)
num1=0
#print(data)
for k in range(len(data)-1,-1,-1):

    if K_nagasa>k and bink[k]=="1":
        #print(k,"k")
        num=num1+data[k]*(2**k)
        for i in range(k):
            num+=max(N-data[i],data[i])*(2**i)
        numlst.append(num)
        num=num1+max(N-data[k],data[k])*(2**k)
        num1+=(N-data[k])*(2**k)
        k-=1

        if k>=0:
            while k>0 and bink[k]!="1":
                num+=data[k]*(2**k)
                k-=1
            num+=data[k]*(2**k)
            if bink[k]!="1":
                for i in range(k):
                    num+=max(N-data[i],data[i])*(2**i)
        numlst.append(num)


    else:
        num1+=data[k]*(2**k)
    numlst.append(num1)
print(max(numlst))
