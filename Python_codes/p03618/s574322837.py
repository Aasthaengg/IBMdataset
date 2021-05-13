# AGC019B - Reverse and Compare
from collections import Counter


def main():
    S = input().rstrip()
    C, N = Counter(S).values(), len(S)
    ans = N * (N - 1) // 2 + 1  # all possible patterns
    ans -= sum(i * (i - 1) // 2 for i in C)  # duplicates
    print(ans)


if __name__ == "__main__":
    main()