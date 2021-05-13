from math import gcd
from functools import reduce
NUM_MAX = 10**6 + 1
def solve(n, a):
    c = [0] * NUM_MAX
    for x in a:
        c[x] += 1
    t = any(sum(c[i::i]) > 1 for i in range(2, NUM_MAX))
    t += reduce(gcd, a) > 1
    return ["pairwise", "setwise", "not"][t] + " coprime"

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
