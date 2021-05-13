n,W=map(int,input().split())

v1=[]
v2=[]
v3=[]
v4=[]

w,v=map(int,input().split())
v1.append(v)
w1=w

for _ in range(n-1):
    w,v=map(int,input().split())
    if w1==w:
        v1.append(v)
    elif w1+1==w:
        v2.append(v)
    elif w1+2==w:
        v3.append(v)
    elif w1+3==w:
        v4.append(v)

v1.sort(reverse=True)
v2.sort(reverse=True)
v3.sort(reverse=True)
v4.sort(reverse=True)

v=[v1,v2,v3,v4]

sumv=[[] for _ in range(4)]

for i,item in enumerate(v):
    tmp=[0]
    tmpv=0
    for j in item:
        tmpv+=j
        tmp.append(tmpv)
    sumv[i]=tmp

ans=0
#print(sumv)
for num1 in range(len(sumv[0])):
    for num2 in range(len(sumv[1])):
        for num3 in range(len(sumv[2])):
            for num4 in range(len(sumv[3])):

                tmpans=0
                tmpwait=0
                if sumv[0][num1]!=0:
                    tmpans+=sumv[0][num1]
                    tmpwait+=(num1)*(w1)
                if sumv[1][num2]!=0:
                    tmpans+=sumv[1][num2]
                    tmpwait+=(num2)*(w1+1)
                if sumv[2][num3]!=0:
                    tmpans+=sumv[2][num3]
                    tmpwait+=(num3)*(w1+2)
                if sumv[3][num4]!=0:
                    tmpans+=sumv[3][num4]
                    tmpwait+=(num4)*(w1+3)

                if tmpwait<=W:
                    ans=max(ans,tmpans)

print(ans)




            

        
