n, m = map(int, input().split())
l = [[0]*n for _ in range(m)]
for i in range(m):
  k, *s = map(int, input().split())
  for j in range(k):
    l[i][s[j]-1] = 1
p = list(map(int, input().split()))

ans = 0
str = '{:0'+str(n)+'b}'
for i in range(2**n):
  s = list(map(int, str.format(i)))
  b = True
  for j in range(m):
    if sum([x & y for x, y in zip(s, l[j])]) % 2 != p[j]:
      b = False
  if b:
    ans += 1

print(ans) 