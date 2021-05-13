from collections import defaultdict
N, C = map(int, input().split())
D = []
for i in range(C):
    K = list(map(int, input().split()))
    D.append(K)
Before = []
for i in range(N):
    K = list(map(int, input().split()))
    Before.append(K)
Num = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        Num[i][j] = (i + j + 2) % 3
Zero = defaultdict(int)
One = defaultdict(int)
Two = defaultdict(int)

for i in range(N):
    for j in range(N):
        if Num[i][j] == 0:
            Zero[Before[i][j] - 1] += 1
        elif Num[i][j] == 1:
            One[Before[i][j] - 1] += 1
        else:
            Two[Before[i][j] - 1] += 1
Cost = [[0]*C for _ in range(3)]
for i in range(C):
    for k, v in Zero.items():
        Cost[0][i] += v * D[k][i]
    for k, v in One.items():
        Cost[1][i] += v * D[k][i]
    for k, v in Two.items():
        Cost[2][i] += v * D[k][i]
ans = float("inf")
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i != j and j != k and k != i:
                ans = min(ans, Cost[0][i] + Cost[1][j] + Cost[2][k])
print(ans)