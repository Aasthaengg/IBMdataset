N, K = map(int, input().split())
moves = [tuple(map(int, input().split())) for _ in range(K)] #Sを構成する区間の情報
MOD = 998244353

DP = [0 for _ in range(N)] #DP[n]で0からnまで動く動き方の数
DP[0] = 1
DP_sum = [0 for _ in range(N)] #のちのためにDPの累積和を格納するための配列を確保する
DP_sum[0] = 1

for n in range(1,N):
  # やりたいこと DP[n] = Σ_(集合Sに属するiについて) DP[n-i]
  # しかし、上記右辺の和を愚直に計算するとTLEする
  # → Sが区間10個以下の和集合であることに注目。区間和は、累積和の差を使えばO(1)で計算できる。
  for l,r in moves:
    # DP[n] += DP[n-l] + DP[n-l-1] + … + DP[n-r]の計算
    if n-l >= 0:
      DP[n] += DP_sum[n-l]
      if n-r-1 >= 0: #右端が-1に到達する場合には、以下の処理は行わない。
        DP[n] -= DP_sum[n-r-1]
    DP[n] %= MOD
    
  DP_sum[n] = (DP_sum[n-1] + DP[n]) % MOD #次以降のnのため、累積和を更新
  
print(DP[N-1] % MOD)
  
