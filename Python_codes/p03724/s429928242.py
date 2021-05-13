# AGC014B - Unplanned Queries
from collections import Counter


def main():
    # all vertices need to appear even times in A
    *A, = map(int, open(0).read().split())
    T = Counter(A[2:]).values()
    flg = any(i % 2 for i in T)
    print("NO" if flg else "YES")


if __name__ == "__main__":
    main()