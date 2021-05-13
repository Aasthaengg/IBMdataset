
from collections import Counter
N = int(input())
V = list(map(int, input().split()))
evens = Counter(V[0::2]).most_common()
odds = Counter(V[1::2]).most_common()
evens.append((0, 0))
odds.append((0, 0))

if evens[0][0] == odds[0][0]:
    print(min(N - evens[1][1] - odds[0][1], N - evens[0][1] - odds[1][1]))
else:
    print(N - evens[0][1] - odds[0][1])