import sys
readline=sys.stdin.readline
x,a,b=map(int,readline().split())

print(['A','B'][abs(x-a)>abs(x-b)])
