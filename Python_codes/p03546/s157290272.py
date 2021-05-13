H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]

A = []
for _ in range(H):
    A += list(map(int, input().split()))

for i in range(10):
    for j in range(10):
        for k in range(10):
            C[j][k] = min(C[j][k], C[j][i]+C[i][k])

from collections import Counter
Co = Counter(A)
ans = 0
for a, c in Co.most_common():
    if a==-1 or a==1:
        continue
    ans += C[a][1]*c
print(ans)