import math
N, P = map(int, input().split())
A = list(map(int, input().split()))
div = 0
for a in A:
  if a % 2 == 1:
    div += 1

ans = 0
mlt = 2 ** (N-div)
if P == 0:
  for i in range(0, div+1, 2):
    cmb = math.factorial(div) // (math.factorial(div-i) * math.factorial(i))
    ans += cmb * mlt
else:
  for i in range(1, div+1, 2):
    cmb = math.factorial(div) // (math.factorial(div-i) * math.factorial(i))
    ans += cmb * mlt
    
print(ans)