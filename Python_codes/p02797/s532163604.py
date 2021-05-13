n, k, s = map(int, input().split())
if s == 10**9:
    ans = [1 for i in range(n)]
else:
    ans = [s+1 for i in range(n)]

for i in range(k):
    ans[i] = s
print(*ans)
