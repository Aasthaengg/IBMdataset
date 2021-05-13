n,m,l=map(int,input().split())
a=[list(map(int,input().split()))for _ in[0]*n]
b=[list(map(int,input().split()))for _ in[0]*m]
for c in a:print(*[sum(s*t for s,t in zip(c,l))for l in zip(*b)])
