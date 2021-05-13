n,k=map(int,input().split())

import math
result = 0
for i in range(1,n+1):
  num_exp = math.log2(k/i)
  num_exp = max(math.ceil(num_exp),0)
  result += (1/n) * ((1/2)**num_exp)
print(result)