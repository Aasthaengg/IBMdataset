import sys
input = sys.stdin.readline
from collections import *

K = int(input())
N = 50
s, a = divmod(K, N)
ans = [N-1+s]*N

for i in range(a):
    ans[i] += N
    
    for j in range(N):
        if i!=j:
            ans[j] -= 1

print(N)
print(*ans)