import math
from scipy.special import comb
n, p = map(int, input().split())
aa = list(map(int, input().split()))
odd = []
even = []
for i in range(n):
  if aa[i] % 2 == 0:
    even.append(aa[i])
  else:
    odd.append(aa[i])
    
x = len(odd)
y = len(even)


sum1 = 0
for i in range(0, x+1, 2):
  sum1 += comb(x,i)
sum2 = 0
for i in range(1, x+1, 2):
  sum2 += comb(x,i)
  
if p == 0:
  ans = int((2 ** y) * sum1)
else:
  ans = int((2 ** y) * sum2)
print(ans)