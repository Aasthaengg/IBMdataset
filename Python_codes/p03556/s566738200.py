import math
N = int(input())
ans = 0
for i in range(int(math.sqrt(N))+1):
  if i * i <= N:
    ans = i*i
print(ans)