import math

N, A, B = [int(_) for _ in input().split()]
H = [int(input()) for _ in range(N)]


def chk(k):
    a_cnt = 0
    for h in H:
        tmp = h - B * k
        if tmp > 0:
            a_cnt += math.ceil(tmp / (A - B))
    return k >= a_cnt


def find(l, r):
    if l > r: return l
    m = (l + r) // 2
    if chk(m):
        r = m - 1
    else:
        l = m + 1
    return find(l, r)


print(find(0, 10 ** 9))
