MOD = 998244353
N, K = list(map(int, input().split()))

a = [0] * (N+1)
f = [0] * (N+1)
mv = list()
for i in range(K):
    mv.append(list(map(int, input().split())))

def solve(N, a, f):
    for i in range(1, N+1):
        f[i] = (f[i-1] + a[i]) % MOD
        for j in range(len(mv)):
            l, r = mv[j]
            if i+l < N+1: a[i+l] = (a[i+l] + f[i]) % MOD
            if i+r+1 < N+1: a[i+r+1] = (a[i+r+1] - f[i]) % MOD

a[1] = 1
mv.sort()
solve(N, a, f)

print(a[N])
