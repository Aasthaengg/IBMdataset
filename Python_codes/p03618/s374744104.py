from collections import Counter


def comb2(n):
    return (n * (n-1)) // 2


A = input()
N = len(A)
c = Counter(A)

print(1 + comb2(N) - sum([comb2(x) for x in c.values()]))
