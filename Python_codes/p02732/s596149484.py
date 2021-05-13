from collections import Counter
from operator import mul
from functools import reduce
import sys
input = sys.stdin.readline

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * N
    cnt = Counter(A)
    s = 0
    for key, value in cnt.items():
        if value < 2:
            continue
        s += combinations_count(value, 2)
    
    for i in range(N):
        if cnt[A[i]]-1 == 0:
            ans[i] = s
        elif cnt[A[i]]-1 == 1:
            ans[i] = s - combinations_count(cnt[A[i]], 2)
        else:
            ans[i] = s - combinations_count(cnt[A[i]], 2) + combinations_count(cnt[A[i]]-1, 2)
    
    print(*ans, sep="\n")

main()