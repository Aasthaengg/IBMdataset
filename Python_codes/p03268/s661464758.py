import math

nk = input().split()
n = int(nk[0])
k = int(nk[1])
res = 0

if k % 2 == 1:
    # a b c equiv 0 mod k
    res = int(math.pow(math.floor(n / k), 3))
else:
    mk0 = 0
    mkk2 = 0
    for i in range(1, n+1):
        if i % k == 0:
            mk0 += 1
        if i % k == (k / 2):
            mkk2 += 1
    res = int(math.pow(mk0, 3) + math.pow(mkk2, 3))

print(res)
