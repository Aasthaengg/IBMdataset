N=int(input())
A=list(map(int,input().split()))

ans,x=0,0
wa,haita=0,0
for j in range(N):
    while x<N and haita^A[x]==wa+A[x]:
        haita^=A[x]
        wa+=A[x]
        x+=1
    ans+=x-j
    haita^=A[j]
    wa-=A[j]
print(ans)