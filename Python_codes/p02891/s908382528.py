from itertools import groupby

S = input()
K = int(input())
grp = [[k, len(list(g))] for k, g in groupby(S)]  # grp[文字][個数]
if len(grp) == 1:
    print(grp[0][1] * K // 2)
else:
    head = grp[0][1]
    tail = grp[-1][1]
    body_sum = 0
    for g in grp[1:len(grp) - 1]:
        body_sum += g[1] // 2 * K
    if grp[0][0] == grp[-1][0]:
        print(head // 2 + tail // 2 + (head + tail) // 2 * (K - 1) + body_sum)
    else:
        print(head // 2 * K + tail // 2 * K + body_sum)
