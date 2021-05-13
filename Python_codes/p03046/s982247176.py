M, K = map(int, input().split())
A = iter(range(2**19))
S = set()
D = []
if K==0:
    for i in range(2**M):
        D += [i, i]
    print(*D)
    exit()
while True:
    while True:
        a = next(A)
        if K^a not in S: break
    S |= {a}
    while True:
        b = next(A)
        if K^b not in S: break
    S |= {b}
    if b >= 2**M or K^b >= 2**M or K^a >= 2**M:
        print(-1)
        exit()
    D += [a, K^a, b, K^b, K^a, a, K^b, b]
    if len(D)==2**(M+1):
        break
print(*D)