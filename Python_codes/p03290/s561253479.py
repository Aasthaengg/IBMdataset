import math

D, G = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(D)]

ret = 1000 ** 10
for i in range(2 ** D):
    total = 0
    cnt = 0
    digit = 1
    for p in range(D):
        if (digit << p) & i:
            cnt += lst[p][0]
            total += lst[p][0] * (p + 1) * 100 + lst[p][1]

    for p in range(D)[::-1]:
        if not ((digit << p) & i):
            delta = max(0, G - total)
            n = min(math.ceil(delta / ((p + 1) * 100)), lst[p][0])
            cnt += n
            total += n * (p + 1) * 100
    ret = min(ret, cnt)
print(ret)
