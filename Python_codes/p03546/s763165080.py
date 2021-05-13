H, W = map(int, input().split())
C = []
for _ in range(10):
    C.append(list(map(int, input().split())))

# solve
for k in range(10):
    for i in range(10):
        for j in range(10):
            if C[i][j] > C[i][k] + C[k][j]:
                C[i][j] = C[i][k] + C[k][j]

from collections import Counter
cnt = Counter()
for __ in range(H):
    # A.append(list(map(int, input().split())))
    cnt.update(list(map(int, input().split())))

ans = 0
for i in cnt.keys():
    if i == -1:
        continue
    ans += C[i][1] * cnt[i]

print(ans)