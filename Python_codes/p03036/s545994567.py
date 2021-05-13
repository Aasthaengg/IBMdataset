import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


r,D,x = MI()
for _ in range(10):
    x = r*x-D
    print(x)

