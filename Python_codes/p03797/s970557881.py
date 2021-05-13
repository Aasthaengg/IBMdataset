n, m = map(int, input().split())
if n * 2 >= m:
  print(m // 2)
  exit()
res = n
m -= (2 * n)
res += (m // 4)
print(res)