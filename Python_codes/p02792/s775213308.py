from collections import Counter
n = int(input())
li = [(int(str(x)[0]), int(str(x)[-1])) for x in range(1, n + 1)]

c = dict(Counter(li).items())

cnt = 0
for k, v in c.items():
    a, b = k
    if a == b:
        cnt += v**2
    elif (b, a) in c:
        v2 = c[(b, a)]
        cnt += v * v2

print(cnt)