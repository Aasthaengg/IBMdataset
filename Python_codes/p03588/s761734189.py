import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N = I()
X = [tuple(MI()) for _ in range(N)]
X.sort()
print(sum(X[-1]))
