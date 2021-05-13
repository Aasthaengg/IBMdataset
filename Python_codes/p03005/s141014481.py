import sys
sys.setrecursionlimit(1000000)
 
N,K = map(int,input().split())

if K == 1:
    print(0)
else:
    print(N-K)