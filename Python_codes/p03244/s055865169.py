
from collections import Counter

N = int(input())
X = list(map(int, input().split()))

evens = Counter(X[::2]).most_common()
odds = Counter(X[1::2]).most_common()

evens.append((0, 0))
odds.append((0, 0))

if evens[0][0] != odds[0][0]:
    print(N - evens[0][1] - odds[0][1])
else:
    print(min(N - evens[0][1] - odds[1][1], N - evens[1][1] - odds[0][1]))
