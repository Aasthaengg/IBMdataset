import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,K = MI()
print(N-K+1)
