from collections import defaultdict
import itertools

n, c = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(c)]
C = [list(map(int, input().split())) for _ in range(n)]

dic = [defaultdict(int) for _ in range(3)]

for i in range(n):
    for j in range(n):
        dist = (i+j) % 3
        num = C[i][j] - 1
        dic[dist][num] += 1


value = [[] for _ in range(3)]
for distance in range(3):
    count_dic = dic[distance]
    for color in range(c):
        res = 0
        for num, count in count_dic.items():
            point = D[num][color] * count
            res += point

        value[distance].append([res, color])

for i in range(3):
    value[i].sort()

A = value[0][:3]
B = value[1][:3]
C = value[2][:3]

ans = 10**9
patterns = itertools.product(A, B, C)
for pattern in patterns:
    (v1, color1), (v2, color2), (v3, color3) = pattern
    check = {color1, color2, color3}
    if len(check) != 3:
        continue
    ans = min(ans, v1+v2+v3)

print(ans)