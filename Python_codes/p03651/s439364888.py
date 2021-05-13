"""
KがAの最大公約数の倍数であれば実現可能。そうでなければ実現不可能。
"""
import sys
sys.setrecursionlimit(200000)
N,K = map(int,input().split())
A = list(map(int,input().split()))

def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
if N ==1:
    g = A[0]
else:
    g = gcd(A[0],A[1])
    for i in range(2,N):
        g = gcd(g,A[2])

if K<=max(A) and K%g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")