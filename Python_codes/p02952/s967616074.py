import math
N = int(input())
digit = int(math.log10(N)) + 1
ans = 0
for i in range(1, digit, 2):
  ans += 9 * (10 ** (i-1))
 
if digit % 2 == 1:
  ans += N - (10 ** (digit - 1) - 1)
 
print(ans)