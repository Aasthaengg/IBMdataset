import sys
from bisect import bisect_left

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    idx = bisect_left(A[1:-1], 0)
    m_group = A[1:1 + idx]
    p_group = A[1 + idx: -1]

    ans = []

    MAX = A[-1]
    for m in m_group:
        ans.append(f"{MAX} {m}")
        MAX -= m

    MIN = A[0]
    for p in p_group:
        ans.append(f"{MIN} {p}")
        MIN -= p

    ans.append(f"{MAX} {MIN}")
    M = MAX - MIN

    print(M)
    print("\n".join(ans))


if __name__ == "__main__":
    main()
