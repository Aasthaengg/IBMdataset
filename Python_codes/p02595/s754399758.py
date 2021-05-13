import math
N, D = map(int, input().split())
P = [list(map(int,input().split())) for i in range(N)]

cnt = 0
for i in range(N):
    d = math.sqrt(int(P[i][0])**2 + int(P[i][1])**2)
    if d <= D:
        cnt += 1

print(cnt)