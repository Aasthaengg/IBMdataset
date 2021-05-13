# ABC105D

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n,m,q = map(int, input().split())
lr = [None] * m
qs = [None] * q

for i in range(m):
    lr[i] = tuple(map(lambda x: int(x)-1, input().split()))
    
t = [[0]*(n+1) for _ in range(n+1)]

for x,y in lr:
    t[y][x] += 1
    
for i in range(n):
    for j in range(i,n):
        t[j][j-i] += t[j-1][j-i] + t[j][j-i+1] - t[j-1][j-i+1]
        
ans = [None] * q
for i in range(q):
    l, r = tuple(map(lambda x: int(x)-1, input().split()))
    ans[i] = t[r][l]
write("\n".join(map(str, ans)))