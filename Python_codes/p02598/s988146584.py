N, K = map(int, input().split())
A = [int(i) for i in input().split()]
l = 0
r = 10 ** 9 + 1
while l + 1 < r:
    p = (l + r) // 2
    n = 0
    ok = False
    for v in A:
        n += (v // p - 1)
        if not v % p == 0:
            n += 1
        if n > K:
            break
    else:
        ok = True
    if not ok:
        l = p
    else:
        r = p

print(r)

