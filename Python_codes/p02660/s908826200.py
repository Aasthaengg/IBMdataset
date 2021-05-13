N = int(input())
ans = 0

## execute
d = 2
while d*d <= N:
  if N % d == 0:
    z = d
    while N % z == 0:
      N /= z
      ans += 1
      z *= d
    while N % d == 0:
      N /= d
  d += 1

if N > 1: ans += 1 # N is prime
print(ans)