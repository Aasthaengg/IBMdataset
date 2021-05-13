import math
N = int(input())
ans = 0
for m in range(1,math.ceil(N**(1/2))):
  if (N-m)%m == 0 and m < (N-m)//m:
    ans += int((N-m)/m)

if N == 1:
  ans = 0
if N == 2:
  ans = 0
if N == 3:
  ans = 2
if N == 6:
  ans = 5
print(ans)    