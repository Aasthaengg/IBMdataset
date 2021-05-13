import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    N = int(input())
    ht = defaultdict(int)

    for i in range(1, N + 1):
        k = i
        head = k % 10
        while k >= 10:
            k //= 10
        tail = k
        if head > 0: ht[(head, tail)] += 1
    ans = 0
    for i in range(1, N + 1):
        k = i
        tail = k % 10
        while k >= 10:
            k //= 10
        head = k
        if tail > 0: ans += ht[(head, tail)]
    print(ans)

    return 0

if __name__ == "__main__":
    solve()