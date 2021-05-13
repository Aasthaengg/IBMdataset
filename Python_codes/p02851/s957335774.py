import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *A = map(int, read().split())

    A = [(a - 1) % K for a in A]

    csum = [0] * (N + 1)
    for i in range(N):
        csum[i + 1] = (csum[i] + A[i]) % K

    indices = defaultdict(list)
    for i in range(N + 1):
        indices[csum[i]].append(i)

    ans = 0
    for vec in indices.values():
        right = 0
        for left in range(len(vec)):
            while right + 1 < len(vec) and vec[right + 1] - vec[left] < K:
                right += 1

            ans += right - left
            if left == right:
                right += 1

    print(ans)

    return


if __name__ == '__main__':
    main()
