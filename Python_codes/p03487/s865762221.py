import math
import collections
import fractions
import itertools

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = collections.Counter(a)
    ans = 0
    for i in c:
        if c[i] >= i:
            ans += c[i] - i
        else:
            ans += c[i]
    print(ans)
    return 0

if __name__ == '__main__':
    solve()