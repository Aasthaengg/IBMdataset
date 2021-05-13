import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
tmp = list(map(int, input().split()))
# 偶奇で分けて辞書作る
odd = defaultdict(int)
even = defaultdict(int)
for i in range(n):
    if i % 2 == 0:
        odd[tmp[i]] += 1
    else:
        even[tmp[i]] += 1

# 降順ソート
odd = sorted(odd.items(), key=lambda x: -x[1])
even = sorted(even.items(), key=lambda x: -x[1])
# 各配列の最頻，二番目を取ってくる
o1 = odd[0]
e1 = even[0]
# 1種類しかない場合は適当に二番目を作成
if len(odd) != 1:
    o2 = odd[1]
else:
    o2 = (0, 0)
if len(even) != 1:
    e2 = even[1]
else:
    e2 = (0, 0)

# 最多文字が異なる
if o1[0] != e1[0]:
    print(n - (o1[1] + e1[1]))
# 最多文字が同じ
else:
    ans = min((n - (o2[1] + e1[1])), (n - (o1[1] + e2[1])))
    print(ans)
