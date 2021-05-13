import sys
input = sys.stdin.readline
n,p = [int(i) for i in input().split()]
s = input()
ans = 0

import math
def nCr(n, r):
  if n < r:
    return 0
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i + 1
    print(ans)
    exit()

else:
  chk = [0]*p
  chk[0] = 1
  m = 0
  for i in range(n)[::-1]:
    m = (int(s[i])*pow(10,n-1-i,p)+m)%p
    chk[m] += 1
  for i in chk:
    ans += nCr(i,2)
  print(ans)
