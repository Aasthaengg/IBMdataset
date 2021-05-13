N=int(input())
ans=2*10**9
for i in range(N):
    ans=min(ans,sum(list(map(int,input().split()))))
print(ans)