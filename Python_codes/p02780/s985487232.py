n,k = map(int, input().split())
l = list(map(int, input().split()))

# 期待値:マス目の総和／マス目の数, マス目の最大値+最小値[1]／2
l = [(i+1)/2 for i in l] # 期待値に変換

# 累積和を取得
from itertools import accumulate
cum = [0] + list(accumulate(l))

# 差分を考慮しつつ k個の和をリストする → 最大値が ans
sum_k = []
for j in range(n-k+1):
    sum_k.append(cum[k+j] - cum[j])

print(max(sum_k))
