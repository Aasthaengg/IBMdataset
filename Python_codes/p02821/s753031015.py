import sys
input = sys.stdin.readline
from bisect import *

def judge(x):
    cnt = 0
    
    for Ai in A:
        cnt += N-bisect_left(A, x-Ai)
    
    return cnt>=M

def binary_search():
    l, r = 0, 10**10+100
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            l = m+1
        else:
            r = m-1
    
    return r

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
acc = [0]

for Ai in A:
    acc.append(acc[-1]+Ai)

b = binary_search()
ans = 0
cnt = 0

for Ai in A:
    i = bisect_left(A, b+1-Ai)
    ans += (N-i)*Ai+acc[N]-acc[i]
    cnt += N-i

ans += (M-cnt)*b
print(ans)
