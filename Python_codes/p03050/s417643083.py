from math import sqrt
N = int(input())
M = int((sqrt(4*N+1)-1)/2)
ans = 0
a = 1
while a <= M:
  if N % a == 0:
    m = N // a - 1
    ans += m if m > 0 and N % m == a else 0
  a += 1
print(ans)