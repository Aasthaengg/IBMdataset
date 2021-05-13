N = int(input())
A = list(map(int, input().split()))

from collections import Counter

ctr = Counter(A)

n_even = len([1 for v in ctr.values() if v%2 == 0])

if n_even % 2 == 0:
    print(len(ctr))
else:
    print(len(ctr)-1)