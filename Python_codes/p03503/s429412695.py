from itertools import product
N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

ans = -(10 ** 30)
for p in product(range(2), repeat=10):
    if sum(p) == 0: continue
    tmp = 0
    for i in range(N):
        # お店ごとにかぶっている日数を数える
        cnt = 0
        for j in range(10):
            if p[j] and F[i][j]:
                cnt += 1
        tmp += P[i][cnt]
    ans = max(ans, tmp)
print(ans)
