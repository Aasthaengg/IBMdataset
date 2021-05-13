from fractions import gcd

n, k = map(int, input().split())
a = [int(x) for x in input().split()]
key = a[0]
for i in range(1, n):
  key = gcd(key, a[i])

if k > max(a):
  ans = False
elif key == 1:
  ans = True
elif k%key == a[0]%key:
  ans = True
else:
  ans = False

if ans:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")