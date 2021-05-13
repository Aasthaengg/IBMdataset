N = int(input())
INF = 1<<22
a = [int(c) for c in input().split()]+[INF]
l = 0
r = 1
s = a[l]
x = a[l]
ans = 0
for l in range(N):
  if l==r:
    r += 1
  while r<=N:
    if s!=x:
      break
#    print(a[r])
    s += a[r]
    x ^= a[r]
    r += 1
  s -= a[l]
  x ^= a[l]
  ans += r-l-1
#  print(l,r)
print(ans)