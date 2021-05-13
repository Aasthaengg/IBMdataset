
N,M = map(int, input().split())
MOD = 10**9 + 7

if abs(N-M) > 1:
    print(0)
    exit()

n_res = 1
for i in range(1,N+1):
    n_res = i * n_res % MOD

m_res = 1
for i in range(1,M+1):
    m_res = i * m_res % MOD

if N == M:
    print((n_res **2 * 2) % MOD)
else:
    print((n_res * m_res) % MOD)
