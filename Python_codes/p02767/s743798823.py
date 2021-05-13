import numpy as np
 
N = input()
X = list(map(int, input().split()))
ans=9999999
for P in range(0, 101):
  sum = np.sum(list(map(lambda x: (x-P)**2, X)))
  ans = min(ans, sum)
    
print(ans)