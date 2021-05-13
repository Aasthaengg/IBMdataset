###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N, M = mi()
Ss = list(mi())
Ts = list(mi())
slen = len(Ss)
tlen = len(Ts)

#DPを2つ作る
#1スタートにしておく。0は、for分でindexエラーを出さないために使う
DP_pairs = [[0] * (len(Ts)+1) for _ in range(len(Ss)+1)] #末尾がS[i]==T[j]である共通部分列の数
DP_cumsum = [[0] * (len(Ts)+1) for _ in range(len(Ss)+1)] #二次元累積和


for i, s in enumerate(Ss):
  i += 1 #1スタート
  for j, t in enumerate(Ts):
    j += 1 #1スタート
    if s==t:
      DP_pairs[i][j] = DP_cumsum[i-1][j-1] + 1
    #s!=tの場合はほっといてもDP_pairsが0なので何もする必要なし
    DP_cumsum[i][j] = (DP_cumsum[i][j-1]+DP_cumsum[i-1][j]-DP_cumsum[i-1][j-1]+DP_pairs[i][j])%(10**9+7)

print(DP_cumsum[len(Ss)][len(Ts)]+1)
