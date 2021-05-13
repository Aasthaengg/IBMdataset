n = int(input())
a = list(map(int, input().split()))
s = sum(a)
si = 0
ans = 10 ** 18
for i in range(len(a) - 1):
  si += a[i]
  ans = min(ans, abs(2 * si - s))
print(ans)
