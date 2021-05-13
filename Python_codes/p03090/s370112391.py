
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
edge = []
if N&1:
    cnt = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i+j != N:
                edge.append((i,j))
                cnt += 1

else:
    cnt = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i+j != N+1:
                edge.append((i,j))
                cnt += 1

print(cnt)
for u,v in edge:
    print(u,v)