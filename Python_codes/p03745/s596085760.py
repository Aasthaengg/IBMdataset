N=int(input())
A=list(map(int,input().split()))

ans=1
x=y=0
c=A[0]

for i in range(1,N):
    if c < A[i]:
        x=1
    elif c>A[i]:
        y=1
    
    if x==1 and y==1:
        ans+=1
        x=y=0
    
    c=A[i]

print(ans)