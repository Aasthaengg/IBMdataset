# E - This Message Will Self-Destruct in 5s
from bisect import *
N = int(input())
A = list(map(int,input().split()))
l = []
ans = 0
for j in range(N):
    tmp = j-A[j]
    ans += bisect_right(l,tmp)-bisect_left(l,tmp)
    insort(l,A[j]+j)
print(ans)