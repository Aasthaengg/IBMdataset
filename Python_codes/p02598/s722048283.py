# E - Logs
import sys
sys.setrecursionlimit(1000000)

N,K = map(int,input().split())
A = list(map(int,input().split()))

def rec(l,r):
    global N,K,A
    if l==r:
        return l
    tmp = (l+r)//2
    ans = 0
    for i in range(N):
        ans += (A[i]-0.001)//tmp
    if ans<=K:
        return rec(l,tmp)
    else:
        return rec(tmp+1,r)
    
print(rec(1,max(A)))