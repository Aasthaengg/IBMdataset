n = int(input())
l = list(map(int, input().split()))

from collections import Counter
c = Counter(l)

total = 0
for i in c.values():
    if i != 1:
        total += i*(i-1)//2 # 組み合わせ_重複なしの数の公式を整理

for j in range(n): # 影響する部分のみ再計算(引く→足す)する
    tmp = c[l[j]]
    before = tmp*(tmp-1)//2 
    after = (tmp-1)*(tmp-2)//2
    print(total - before + after)
