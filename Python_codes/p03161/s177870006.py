import sys
sys.setrecursionlimit(10**7)
n,k = [int(x) for x in input().split()]
h = [int(x) for x in input().split()]
memo = [0]*n
for i in range(1, n):
    min_k = float('inf') 
    min_k=min([memo[j] +abs(h[i]-h[j]) for j in range(max(0, i-k), i)])
    memo[i] = min_k

print(memo[-1])
