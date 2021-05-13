import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


n,m,d = MI()
print((2*(m-1)*(n-d))/(n**2) if d != 0 else ((m-1)*(n-d))/(n**2))
