n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

from collections import Counter
ca = Counter(a)

# 個数が少ないものを何個削れば良いか数える
c = sorted(ca.values())
print(sum(c[:-k]))