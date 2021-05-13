from collections import Counter
import itertools
n, k = map(int, input().split())
d = []
sunuke = []
for i in range(k):
    d.append(int(input()))
    sunuke.append(list(map(int, input().split())))

new = list(itertools.chain.from_iterable(sunuke))

c = Counter(new)

print(n - len(c))
