class Combination:                                      # 計算量は O(n_max + log(mod))
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max+1):                     # 階乗(= n_max !)の逆元を生成
            f = f * i % mod                             # 動的計画法による階乗の高速計算
            fac.append(f)                               # fac は階乗のリスト
        f = pow(f, mod-2, mod)                          # 階乗から階乗の逆元を計算。フェルマーの小定理より、　a^-1 = a^(p-2) (mod p) if p = prime number and p and a are coprime
                                                        # python の pow 関数は自動的に mod の下での高速累乗を行ってくれる
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):                   # 上記の階乗の逆元から階乗の逆元のリストを生成（＝ facinv ）
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()


    def __call__(self, n, r):  # self.C と同じ
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def P(self, n, r):
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[n-r] % self.mod

##############################################################################################
import sys
input = sys.stdin.readline

mod=10**9+7
N, K = map(int, input().split())
comb = Combination(K)
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append(b)
    edges[b].append(a)

res = K
res *= comb.P(K-1,len(edges[0]))
res %= mod
next_set = edges[0]
visited = set([0]+edges[0])
while next_set:
    p = next_set.pop()
    cnt = 0
    for q in edges[p]:
        if q in visited:
            continue
        cnt += 1
        visited.add(q)
        next_set.append(q)
    res *= comb.P(K-2,cnt)
    res %= mod
print(res%mod)