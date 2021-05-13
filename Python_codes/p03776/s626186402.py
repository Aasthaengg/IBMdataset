import sys
from itertools import accumulate
from collections import defaultdict
from operator import mul
from functools import reduce
def input(): return sys.stdin.readline().strip()

def comb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
    N, A, B = map(int, input().split())
    V = list(map(int, input().split()))
    V.sort(reverse=True)

    num_kind = defaultdict(int)
    same_kind = [1] * N
    pre = V[0]
    num_kind[V[0]] += 1
    for i in range(1, N):
        num_kind[V[i]] += 1
        if pre == V[i]:
            same_kind[i] = same_kind[i - 1] + 1
        pre = V[i]

    S = [0] + list(accumulate(V))
    average = defaultdict(int)
    max_val = 0
    for i in range(A, B + 1):
        val = S[i] / i
        if val >= max_val:
            max_val = val
            n, r = num_kind[V[i - 1]], same_kind[i - 1]
            average[max_val] += comb(n, r)
    print(max_val)
    print(average[max_val])



if __name__ == "__main__":
    main()
