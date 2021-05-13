n, a, b, c = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
from itertools import product
bamboo = [0, a, b, c]
min_num = float('inf')
for i in product([0, 1, 2, 3], repeat=n):
    if set(i) >= set([1, 2, 3]):
        sums = [0, 0, 0, 0]
        tmp = -30
        for j in range(n):
            if i[j] != 0:
                sums[i[j]] += l[j]
                tmp += 10
        min_num = min(min_num,tmp+sum(abs(sums[k] - bamboo[k]) for k in range(1, 4)))
print(min_num)