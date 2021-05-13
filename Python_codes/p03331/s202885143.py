def ds(x):
  ret = 0
  while x > 0:
    ret += x % 10
    x //= 10
  return ret

n = int(input())
ans = n
for i in range(1, n):
  ans = min(ans, ds(i) + ds(n-i))
print(ans)