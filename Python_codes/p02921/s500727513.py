import numpy as np
N=input()
M=input()
ans = 0
for i in range(3):
  if N[i]==M[i]:
    ans += 1
print(ans)