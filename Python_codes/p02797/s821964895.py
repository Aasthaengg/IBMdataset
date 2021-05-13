N, K, S = map(int, input().split())
ans = []
for i in range(K):
    ans.append(S)
r = N - K
if S > r:
    for i in range(r):
        ans.append(1)
else:
    for i in range(r):
        ans.append(10**9)
print(*ans)
