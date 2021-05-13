import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


x1,y1,x2,y2 = MI()
dx,dy = y1-y2,x2-x1
print(x2+dx,y2+dy,x1+dx,y1+dy)
