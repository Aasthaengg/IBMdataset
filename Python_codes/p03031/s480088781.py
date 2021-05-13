import math
N, M = list(map(int, input().split()))
q = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

result_count = 0
for i in range(2**N):
    flag = True
    for idx, j in enumerate(q):  # 電球の数分ループ
        tmp_count = 0
        for k in j[1:]:
            if i >> (k - 1) & 1 == 1:
                tmp_count += 1
        if tmp_count % 2 != p[idx]:
            flag = False
    result_count += 1 if flag else 0

print(result_count)
