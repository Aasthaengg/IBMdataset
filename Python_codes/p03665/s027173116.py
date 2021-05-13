import math


N, P = map(int, input().split())
A = list(map(int, input().split()))
B = [a % 2 for a in A]
count_0 = B.count(0)
count_1 = B.count(1)


def comb_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


x = y = 0
if count_0 == 0:
    x = 1
else:
    if P == 1 and count_1 == 0:
        x = 0
    else:
        for i in range(count_0 + 1):
            x += comb_count(count_0, i)

if count_1 == 0:
    y = 1
else:
    if P == 0:
        for i in range(0, count_1 + 1, 2):
            y += comb_count(count_1, i)
    else:
        for i in range(1, count_1 + 1, 2):
            y += comb_count(count_1, i)

print(x * y)
