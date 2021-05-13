N, M = map(int, input().split())
*S, = map(int, input().split())
*T, = map(int, input().split())

data = [0]*(M+2)
def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s % MOD
def add(k, x):
    while k <= M:
        data[k] = (data[k] + x) % MOD
        k += k & -k

MOD = 10**9 + 7
s = 0
rM = range(M-1, -1, -1)
for i in range(N):
    si = S[i]
    for j in rM:
        if si == T[j]:
            v = get(j+1) + 1
            add(j+2, v); s += v
print((s + 1) % MOD)