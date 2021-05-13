import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

a,b = MI()
c = b-a
print(c*(c+1)//2-b)
