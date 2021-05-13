import sys
read=sys.stdin.read

n,*d=map(int,read().split())
d.sort()
print(sum(x<y for x,y in zip(d,d[1:]))+1)