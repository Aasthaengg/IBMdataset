import sys
from collections import Counter
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    AC = accumulate([0] + A, func=lambda x,y:(x+y)%M)
    ACC = Counter(AC)

    ans = 0
    for c in ACC.values():
        ans += c * (c-1) // 2
    print(ans)

if __name__ == '__main__':
    main()