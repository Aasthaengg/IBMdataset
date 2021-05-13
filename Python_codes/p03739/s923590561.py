from itertools import accumulate
n = int(input())
a = list(accumulate([int(i) for i in input().split()]))
d = 0
ans = 0
for i, n in enumerate(a):
    n += d
    if i & 1:
        if n >= 0:
            ans += n + 1
            d -= n + 1
    # 奇数回目でマイナスのとき
    elif n <= 0:
        ans += - n + 1
        d += - n + 1
c = ans
ans = 0
d = 0
for i, n in enumerate(a):
    n += d
    if i & 1 == 0:
        if n >= 0:
            ans += n + 1
            d -= n + 1
    elif n <= 0:
        ans += - n + 1
        d += - n + 1
print(min(ans, c))