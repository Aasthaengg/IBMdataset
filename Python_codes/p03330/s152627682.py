#099_D
from collections import Counter
n, c = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(c)]
C = [list(map(int, input().split())) for _ in range(n)]
C0, C1, C2 = [], [], []
for i in range(n):
    for j in range(n):
        if (i + j) % 3 == 0:
            C0.append(C[i][j]-1)
        elif (i + j) % 3 == 1:
            C1.append(C[i][j]-1)
        else:
            C2.append(C[i][j]-1)
C0 = Counter(C0)
C1 = Counter(C1)
C2 = Counter(C2)

ans = 10 ** 10
for i in range(c):
    for j in range(c):
        if i == j:
            continue
        for k in range(c):
            if i == k or j == k:
                continue
            tmp = 0
            for col, num in C0.items():
                tmp += D[col][i] * num
            for col, num in C1.items():
                tmp += D[col][j] * num
            for col, num in C2.items():
                tmp += D[col][k] * num
            
            ans = min(tmp, ans)
            
print(ans)