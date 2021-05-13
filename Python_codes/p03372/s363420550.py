N, C = map(int, input().split())
X = [0] * N
V = [0] * N
for i in range(N):
    x, v = map(int, input().split())
    X[i] = x
    V[i] = v


answer = 0
R = [0] * N
score = 0
maxscore = 0
for i in range(N):
    score += V[i]
    R[i] = max(maxscore, score - X[i])
    maxscore = R[i]
    answer = max(answer, R[i])

L = [0] *N
score = 0
maxscore = 0
for i in range(N)[::-1]:
    score += V[i]
    L[i] = max(maxscore, score - (C - X[i]))
    maxscore = L[i]
    answer = max(answer, L[i])
L.append(0)

for i in range(N-1):
    answer = max(answer, R[i] - X[i] + L[i+1])

for i in range(1, N)[::-1]:
    answer = max(answer, L[i] - (C-X[i]) + R[i-1])

print(answer)
