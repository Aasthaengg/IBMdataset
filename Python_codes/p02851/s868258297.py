from itertools import accumulate
from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))


# あらかじめ数列から１を引いておく
A = [a - 1 for a in A]

# mod K の累積和を取る
S = [0] + list(accumulate(A))
S = [s % K for s in S]


ans = 0
counter = defaultdict(int)
for i, s in enumerate(S):
    ans += counter[s]  # 過去の出現数を参考に数え上げ

    counter[s] += 1  # 今見たところを追加
    if i - K + 1 >= 0:
        counter[S[i - K + 1]] -= 1  # 条件を見たしうる長さK-1からはみ出たところを取り除く

print(ans)
