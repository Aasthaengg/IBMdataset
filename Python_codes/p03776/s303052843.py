import math
def pcount(n, r):
    return math.factorial(n) // (math.factorial(r)* math.factorial(n - r))

n, a, b = map(int, input().split())
L = [int(i) for i in input().split()]
L.sort(reverse=True)

T = L[:a]
print(sum(T)/a)

s = 0
Tmin = min(T)
countTminT = T.count(Tmin)
countTminL = L.count(Tmin)

if a == 1 and countTminL == 1:
  s = 1
elif countTminT == a:
  for i in range(a,b+1):
    if countTminL+1 == i:
      break
    s += pcount(countTminL, i)
else:
  s += pcount(countTminL, countTminT)

print(s)