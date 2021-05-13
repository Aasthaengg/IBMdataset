import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


a,b,c,d = MI()
print(max(a*c,a*d,b*c,b*d))
