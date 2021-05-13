n,m = map(int,input().split())
x = [0]*n
y = [0]*n
z = [0]*n
for i in range(n):
  x[i],y[i],z[i] = map(int,input().split())
ans = 0
for i in range(2**3):
  s = [0]*n
  a = [1]*3
  j = 0
  while i > 0:
    if i&1:
      a[j] = -1
    i = i >> 1
    j += 1
  for i in range(n):
    s[i] = x[i]*a[0] + y[i]*a[1] + z[i]*a[2]
  s.sort(reverse = True)
  ans = max(ans, sum(s[:m]))
print(ans)
