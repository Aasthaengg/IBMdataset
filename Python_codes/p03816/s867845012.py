from collections import Counter

def solve(n, A):
    c = Counter(A)
    return len(c) - (sum(v - 1 for v in c.values()) % 2)

_n = map(int, input().split())
_A = list(map(int, input().split()))
print(solve(_n, _A))
