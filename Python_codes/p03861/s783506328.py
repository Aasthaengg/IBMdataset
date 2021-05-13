import sys
readline = sys.stdin.readline

a,b,x = map(int,readline().split())

print((b // x) - (a - 1)// x)