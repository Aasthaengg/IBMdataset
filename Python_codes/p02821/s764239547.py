k = 34
K = 1<<k
nu = lambda L: int("".join([bin(K+a)[-k:] for a in L[::-1]]), 2)
st = lambda n: bin(n)[2:] + "0"
li = lambda s: [int(a, 2) if len(a) else 0 for a in [s[-(i+1)*k-1:-i*k-1] for i in range(len(B)*2-1)]]

N, M = map(int, input().split())
A = [int(a) for a in input().split()]
B = [0] * 100001
for a in A:
    B[a] += 1
C = li(st(nu(B) ** 2))
ans = 0
for i in range(200001)[::-1]:
    a = min(M, C[i])
    M -= a
    ans += a * i
print(ans)