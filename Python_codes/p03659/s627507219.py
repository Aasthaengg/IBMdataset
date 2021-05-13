N = int(input())
a = list(map(int, input().split()))
s = a[:1]
t = a[1:]
x = sum(s)
y = sum(t)
if x==y:
  ans = 0
else:
  ans = abs(x-y)

for i in range(1,N-1):
  x += a[i]
  y -= a[i]
  if x==y:
    ans = 0
    break
  elif abs(x-y)<ans:
    ans = abs(x-y)
print(ans)