n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
for i in range(n):
  c.append(min(a[i],b[i]))
d = [0 for _ in range(n)]
e = [0 for _ in range(n)]
d[0] = 1
e[-1] = 1
for i in range(1,n):
  if a[i-1] != a[i]:
    d[i] = 1
for i in range(n-1)[::-1]:
  if b[i+1] != b[i]:
    e[i] = 1
for i in range(n):
  if d[i] * e[i] == 1 and a[i] != b[i]:
    print(0)
    break
else:
  for i in range(n):
    if d[i] == 1 and a[i] != c[i]:
      print(0)
      break
    if e[i] == 1 and b[i] != c[i]:
      print(0)
      break
  else:
    ans = 1
    mod = 10 ** 9 + 7
    for i in range(n):
      if d[i] == e[i] == 0:
        ans *= c[i]
        ans %= mod
    print(ans)