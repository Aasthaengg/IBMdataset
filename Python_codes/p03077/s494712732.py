import math
N = int(input())
ABCDE = []
for _ in range(5):
    i = int(input())
    ABCDE.append(i)

X = min(ABCDE)

#ボトルネックに通れる人の数でグループ分けする。
group = math.ceil(N/X)

#3グループに分けられる場合、最後のグループは2分待ってから5分で6に到着する。
ans = (group-1) + 5
print(ans)
