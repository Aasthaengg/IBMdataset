N=int(input())
d=input().split()
D=[list(s) for s in d]
ans=""
for i in range(N):
    ans+=d[0][i]+d[1][i]
print(ans)