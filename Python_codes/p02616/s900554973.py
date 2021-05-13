MOD = 10 ** 9 + 7

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = []
T = []

for a in A:
    if a < 0:
        T.append(a)
    else:
        S.append(a)

lenS = len(S)
lenT = len(T)

ok = False
if lenS > 0:
    if N == K:
        ok = lenT % 2 == 0
    else:
        ok = True
else:
    ok = K % 2 == 0

ans = 1
if not ok:
    A.sort(key=lambda x: abs(x))
    for i in range(K):
        ans *= A[i]
        ans %= MOD
else:
    S.sort()
    T.sort(reverse=True)
    if K % 2 == 1:
        ans *= S.pop()
    P = []
    while len(S) >= 2:
        x = S.pop()
        x *= S.pop()
        P.append(x)
    while len(T) >= 2:
        x = T.pop()
        x *= T.pop()
        P.append(x)
    P.sort(reverse=True)
    for i in range(K//2):
        ans *= P[i]
        ans %= MOD

print(ans)
