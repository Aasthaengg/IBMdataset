N,X=map(int,input().split())
ans=1
L=list(map(int,input().split()))
D=0
for i in range(N):
    D+=L[i]
    ans+=1
    if D>X:
        ans-=1
        break

print(ans)
