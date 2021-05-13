import sys,math,collections,itertools
input = sys.stdin.readline

N=int(input())
zmax=-float('inf')
zmin = float('inf')
wmax = -float('inf')
wmin = float('inf')

for _ in range(N):
    x,y=map(int,input().split())
    z=x+y
    w=x-y
    zmax = max(z,zmax)
    zmin = min(z,zmin)
    wmax = max(w,wmax)
    wmin = min(w,wmin)
print(max(zmax-zmin,wmax-wmin))
