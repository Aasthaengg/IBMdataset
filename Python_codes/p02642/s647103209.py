import sys
from collections import Counter

input = sys.stdin.readline
MAX_A = 10 ** 6


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    divisible = [False] * (MAX_A + 1)
    ans = 0
    for k, v in Counter(A).items():
        if v == 1 and not divisible[k]:
            ans += 1
        for i in range(k, MAX_A + 1, k):
            divisible[i] = True

    print(ans)


if __name__ == "__main__":
    main()
