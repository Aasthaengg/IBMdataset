"""
寿司iまで歩いて食べに行くと、1~iまでの合計カロリー - iまでの移動距離　のカロリーを得られる。
円形なので、時計回りか反時計回りかで移動距離が変わるので、結果のカロリーも変わる。
愚直にやると、
・反時計回りの方向にL個、時計回りの方向にR個食べる
・先にLRどちらに食べに行くか
の選択があるので、N*N*2とかになり、間に合わない。
*2の部分は大したことないので、どちらを先に食べに行くかは全部やっても問題ない。
LとRの決め方について、例えばN=10として、先に左に２個食べる（L=2）とすると、Rは０～８の範囲で選べる。
入店位置から、時計回りに移動して食べて退店するまでのカロリーは、Lまで食べに行く時のカロリーと独立して考えられる。
各Lについてこれを毎回計算するのは処理が重複するので、
・入店位置からRまでのいずれかの寿司へ、時計回りに移動して食べられる時に得られる最大カロリー
を事前に計算しておいて、Lまで食べに行って戻ってきた時のカロリーと合わせればよい。
逆も同様。

これで*Nが一つ消える感じか。
"""
N,C = map(int, input().split())
clocks = [tuple(map(int, input().split())) for _ in range(N)]

antis = []
for x,v in reversed(clocks):
    antis.append((C-x, v))

accum_clocks = [0] * N
accum_clocks[0] = clocks[0][1] - clocks[0][0]
for i in range(1,N):
    accum_clocks[i] = accum_clocks[i-1] + clocks[i][1] - clocks[i][0] + clocks[i-1][0]

# 右にi個まで食べに行ける時に得られる最大カロリー
clocks_max = [0] * (N+1)

for i in range(N):
    clocks_max[i+1] = max(clocks_max[i], accum_clocks[i])

accum_antis = [0] * N
accum_antis[0] = antis[0][1] - antis[0][0]
for i in range(1,N):
    accum_antis[i] = accum_antis[i-1] + antis[i][1] - antis[i][0] + antis[i-1][0]

antis_max = [0] * (N+1)
for i in range(N):
    antis_max[i+1] = max(antis_max[i], accum_antis[i])


ans = 0
ans = max(ans, max(clocks_max), max(antis_max))

# 累積和をカロリーと距離に分けて保存しなかったために面倒になった。
accum_sushi = 0
for l in range(N):
    accum_sushi += antis[l][1]
    #print(l, antis[l][1] - 2*antis[l][0] , clocks_max[N-l-1])
    ans = max(ans, accum_sushi - 2*antis[l][0] + clocks_max[N-l-1])

accum_sushi = 0
for r in range(N):
    accum_sushi += clocks[r][1]
    #print(r, clocks[r][1] - 2*clocks[r][0] , antis_max[N-r-1])
    ans = max(ans, accum_sushi - 2*clocks[r][0] + antis_max[N-r-1])

    
print(ans)
"""
print(accum_clocks)
print(accum_antis)
print(clocks_max)
print(antis_max)
"""