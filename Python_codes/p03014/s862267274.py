h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

U = [[0 for _ in range(w)] for _ in range(h)]
D = [[0 for _ in range(w)] for _ in range(h)]
L = [[0 for _ in range(w)] for _ in range(h)]
R = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            U[i][j] = 0
            L[i][j] = 0
        else:
            if i == 0:
                U[i][j] = 1
            else:
                U[i][j] = U[i - 1][j] + 1
            if j == 0:
                L[i][j] = 1
            else:
                L[i][j] = L[i][j - 1] + 1


for i in reversed(range(h)):
    for j in reversed(range(w)):
        if s[i][j] == "#":
            D[i][j] = 0
            R[i][j] = 0
        else:
            if i == h-1:
                D[i][j] = 1
            else:
                D[i][j] = D[i + 1][j] + 1
            if j == w-1:
                R[i][j] = 1
            else:
                R[i][j] = R[i][j + 1] + 1

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, U[i][j] + D[i][j] + L[i][j] + R[i][j] - 3)

print(ans)