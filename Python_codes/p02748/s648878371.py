A, B, M = map(int, input().split())
Frz = list(map(int, input().split()))
Mic = list(map(int, input().split()))
C = []

for _ in range(M):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    C.append((x,y,c))

minF = min(Frz)
minM = min(Mic)
ans = minF + minM

for x, y, z in C:
    tmp = Frz[x] + Mic[y] - z
    if tmp < ans:
        ans = tmp

print(ans)