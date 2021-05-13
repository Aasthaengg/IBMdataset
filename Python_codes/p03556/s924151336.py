import sys
sys.setrecursionlimit(10**6)
import math

N = int(input())
ans = 1
for i in range(int(math.sqrt(N)+1.1)):
    if i*i <= N:
        ans = max(ans,i*i)

print(ans)