# AGC014B - Unplanned Queries
from collections import Counter


def main():
    N, _, *A = map(int, open(0).read().split())
    T = Counter(A).values()
    flg = all(i % 2 == 0 for i in T)
    print("YES" if flg else "NO")


if __name__ == "__main__":
    main()