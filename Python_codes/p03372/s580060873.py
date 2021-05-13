N, C = map(int, input().split())
D = []
V = [0]

for i in range(N):
    x, v = list(map(int, input().split()))
    D.append(x)
    V.append(V[i] + v)

# clockwise
L = [0]
for i in range(N):
    L.append(max(L[i], V[i + 1] - D[i]))
L_ = max(L)
# counterclockwise
R = [0]
for i in range(N):
    R.append(max(R[i], V[N] - V[N - i - 1] - (C - D[-i - 1])))
R_ = max(R)
# clockwise - counterclockwise
LR = 0
for i in range(N - 1):
    LR = max(LR, V[i + 1] - D[i] * 2 + R[N - i - 1])

# counterclockwise - clockwise
RL = 0
for i in range(N - 1):
    RL = max(RL, V[N] - V[N - i - 1] - (C - D[-i - 1]) * 2 + L[N - i - 1])

print(max(L_, R_, LR, RL))