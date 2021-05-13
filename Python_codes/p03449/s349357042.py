import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))
ans = 0

for i in range(n):
  temp = sum(a[:i+1])+sum(b[i:n])
  ans = max(ans, temp)
print(ans)