# は？なんやこれ無限にわからん
# 半分全列挙的な気持ちでやる？
x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ab = []
for av in a:
    for bv in b:
        ab.append(av + bv)
ab = sorted(ab, reverse=True)[:k]
abc = []
for abv in ab:
    for cv in c:
        abc.append(abv + cv)
abc = sorted(abc, reverse=True)[:k]
for ans in abc:
    print(ans)
