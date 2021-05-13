N=int(input())

if N==1:
    print(1)
    exit()

P=[]
for i in range(N):
    P.append(list(map(int,input().split())))

c={}
for i in range(N):
    for j in range(N):
        if i!=j:
            p=P[j][0]-P[i][0]
            q=P[j][1]-P[i][1]
            temp=str(p)+"_"+str(q)
            if temp in c:
                c[temp]+=1
            else:
                c[temp]=1
c_num=[]
for j in c:
    c_num.append(c[j])

print(N-max(c_num))

