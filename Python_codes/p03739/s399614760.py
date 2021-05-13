import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def solve(A):
    ans = 0
    s = A[0]
    for a in A[1:]:
        prev, s = s, s + a
        if prev > 0 and s >= 0:
            ans += s + 1
            s = -1
        if prev < 0 and s <= 0:
            ans += -s + 1
            s = 1

    return ans


def main():
    N, *A = map(int, read().split())

    if A[0] > 0:
        ans1 = solve(A)
        ans2 = A[0] + 1
        A[0] = -1
        ans2 += solve(A)
        ans = min(ans1, ans2)
    elif A[0] < 0:
        ans1 = solve(A)
        ans2 = -A[0] + 1
        A[0] = 1
        ans2 += solve(A)
        ans = min(ans1, ans2)
    else:
        A[0] = 1
        ans1 = solve(A) + 1
        A[0] = -1
        ans2 = solve(A) + 1
        ans = min(ans1, ans2)

    print(ans)

    return


if __name__ == '__main__':
    main()
