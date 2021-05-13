n = int(input())
a = list(map(int, input().split()))
ans = [0, 0]
s = [0, 0]
for k in range(2):
  for i in range(n):
    t = (i + k) % 2 * 2 - 1
    s[k] += a[i]
    d = max(0, t * s[k] + 1)
    ans[k] += d
    s[k] += -t * d
print(min(ans))
