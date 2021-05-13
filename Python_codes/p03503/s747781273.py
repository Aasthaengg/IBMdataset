N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]
import itertools

ans = 0
for ff, i in enumerate(itertools.product([0, 1], repeat=10)):
    if sum(i) == 0:
        continue
    point = 0
    for idx, f in enumerate(F):
        count = 0
        for a, b in zip(i, f):
            count += a * b
        point += P[idx][count]

    if ff == 1:
        ans = point
    else:
        # if max(ans, point) == point:
        #     print(i)
        ans = max(ans, point)

print(ans)