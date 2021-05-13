import math

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

max_l = max(A) + 1
min_l = 0
cur = (max_l + min_l) // 2


def check(l):
    count = 0
    for a in A:
        count += math.ceil(a / l) - 1

    return count <= K


while True:
    if check(cur):
        max_l = cur + 1
    else:
        min_l = cur

    if cur == (max_l + min_l) // 2:
        break

    cur = (max_l + min_l) // 2

print(cur)
