n, k = map(int, input().split())
hlst = [int(input()) for _ in range(n)]
ans = 10 ** 10
hlst.sort()
k -= 1
for i in range(k, n):
  ans = min(ans, hlst[i] - hlst[i - k])
print(ans)