import math
n, h = map(int, input().split())
shake =[]
throw = []
for _ in range(n):
    a, b = map(int, input().split())
    shake.append(a)
    throw.append(b)

max_shk = max(shake)
sort_thr = sorted(throw, reverse = True)


count = 0
for i in sort_thr:
    if max_shk < i:
        h = h - i
        count += 1
        if h <= 0:
            break
if h > 0:
    count += math.ceil(h / max_shk)
print(count)