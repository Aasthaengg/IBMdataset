import math
import math
N = int(input())
N_MAX = 10 ** 7
table = [1]*N

def get_divisors(n):
  num = 0
  ceil = n
  if n == 1:
    return 1
  for i in range(1, n+1):
    q, mod = divmod(n, i)
    if mod == 0: 
      num += 2
      ceil = q
    if i < ceil: break
  print(n, num)
  return num

ans = 0
for i in range(2,N+1):
  for j in range(1,math.floor(N/i)+1):
    table[i*j-1] += 1

for i, div in enumerate(table):
  ans += (i+1)*div
print(ans)