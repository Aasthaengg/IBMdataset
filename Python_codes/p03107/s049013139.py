from collections import Counter

def solve():
    A = input()
    c = Counter(A)

    return min(c['0'], c['1']) * 2

print(solve())