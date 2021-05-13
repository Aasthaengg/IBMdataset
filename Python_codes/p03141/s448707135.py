N=int(input())
A=[]
B=[]
C=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    c=a+b
    C.append(c)

C.sort(reverse=True)
ans=0
for i in range(N):
    if i%2==0:
        ans+=C[i]

bs=sum(B)
ans-=bs
print(ans)