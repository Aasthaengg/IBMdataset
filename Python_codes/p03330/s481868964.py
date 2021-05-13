from collections import defaultdict

N, C = map(int, input().split())

Disguise = [list(map(int, input().split())) for _ in range(C)]
Color = [list(map(int, input().split())) for _ in range(N)]

C0 = defaultdict(int)
C1 = defaultdict(int)
C2 = defaultdict(int)

for i in range(N):
    for j in range(N):
        if (i + j + 2) % 3 == 0:
            C0[Color[i][j]] += 1
        elif (i + j + 2) % 3 == 1:
            C1[Color[i][j]] += 1
        else:
            C2[Color[i][j]] += 1

ans = float('inf')
for x in range(C):
    for y in range(C):
        for z in range(C):
            if x == y or y == z or z == x:
                continue
            ansi = 0
            for key, value in C0.items():
                ansi += Disguise[key - 1][x] * value
            for key, value in C1.items():
                ansi += Disguise[key - 1][y] * value
            for key, value in C2.items():
                ansi += Disguise[key - 1][z] * value
            ans = min(ansi, ans)
print(ans)
