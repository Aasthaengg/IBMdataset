import fractions
n,k = map(int,input().split())
a = list(map(int, input().split()))
if k > max(a):
  print("IMPOSSIBLE")
  exit()
ans = a[0]
for i in range(1, n):
    ans = fractions.gcd(ans, a[i])
if k%ans == 0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")