N, K, S = map(int,input().split())
ans = []
for k in range(K):
    ans.append(S)
if S < 10**9:
    for k in range(K,N):
        ans.append(10**9)
else:
    for k in range(K,N):
        ans.append(10**9-1)
print(*ans)
