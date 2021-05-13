from itertools import product

N = int(input())
f_lst = [list(map(int, input().split())) for i in range(N)]
p_lst = [list(map(int, input().split())) for i in range(N)]

ret = -10 ** 18
for p in product([0, 1], repeat=10):
    if sum(p) == 0:
        continue
    t = 0
    for i in range(N):
        cnt = 0
        for j in range(10):
            if p[j]:
                cnt += f_lst[i][j]
        t += p_lst[i][cnt]
    ret = max(ret, t)
print(ret)
