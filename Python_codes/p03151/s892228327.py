N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())

Minus=0
Plus=[]
ans=0
for a,b in zip(A,B):
    if a<b:
        ans+=1
        Minus+=b-a
    elif a>b:
        Plus.append(a-b)

Plus.sort()
i=0
M=len(Plus)
Plus=Plus[::-1]
while Minus>0 and i<M:
    ans+=1
    Minus-=Plus[i]
    i+=1

if Minus>0:
    print(-1)
else:
    print(ans)