import sys
import math
ans = 0
N,K = map(int,input().split())
for n in range(1,N+1):
    num = max(0, math.ceil(math.log2(K/n)))
    ans += (1/2)**num

print(ans/N)