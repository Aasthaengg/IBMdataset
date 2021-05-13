import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

K,X = MI()

print(*[i for i in range(X-K+1,X+K)])