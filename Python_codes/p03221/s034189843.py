import sys
input = sys.stdin.buffer.readline

N, M = map(int,input().split())
town = [[] for _ in range(N)]
ans = [0] * M

for i in range(M):
    a, b = map(int,input().split())
    town[a-1].append((b,i))

for i in range(N):
    town[i].sort()
    for k in range(len(town[i])):
        index = town[i][k][1]
        t = town[i][k][0]
        ans[index] = str(i+1).zfill(6) + str(k+1).zfill(6)

for i in ans:
    print(i)
