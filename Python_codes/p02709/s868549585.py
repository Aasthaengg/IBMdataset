import sys

sys.setrecursionlimit(10 ** 9)

input()

arr = list(sorted([(v, idx) for idx, v in enumerate(map(int, input().split()))], reverse=True))

d = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]


def dp(l, r, idx):
    if idx == len(arr):
        return 0

    if d[l][r] != -1:
        return d[l][r]

    left = abs(arr[idx][1] - l) * arr[idx][0] + dp(l + 1, r, idx + 1)
    right = abs(arr[idx][1] - r) * arr[idx][0] + dp(l, r - 1, idx + 1)

    d[l][r] = max(left, right)
    return max(left, right)


print(dp(0, len(arr) - 1, 0))
