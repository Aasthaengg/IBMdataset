N=int(input())
A=[int(input()) for _ in range(N)]

ans=0
if A[0]!=0:
    print(-1)
    exit()
for i in range(N-1,0,-1):
    l,a=A[i-1],A[i]
    if a>l+1:
        print(-1)
        exit()
    elif a==l+1:
        ans+=1
    elif a!=0:
        ans+=a
print(ans)