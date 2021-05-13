import sys
input = sys.stdin.readline


def upper(arr, x):
    # xよりも大きい最小のindexを返す
    if arr[0] > x:
        return 0
    high, low = len(arr), 0
    while high - low > 1:
        mid = (high + low) // 2
        if arr[mid] > x:
            high = mid
        else:
            low = mid
    return high


def lower(arr, x):
    # xよりも小さい最大のindexを返す
    if arr[-1] < x:
        return len(arr) - 1
    high, low = len(arr) - 1, -1
    while high - low > 1:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid
        else:
            high = mid
    return low


A, B, Q = map(int, input().split(' '))
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]

for _ in range(Q):
    x = int(input())
    shr_u, shr_l = upper(s, x), lower(s, x)
    tmp_u, tmp_l = upper(t, x), lower(t, x)
    ans = 10 ** 18
    if shr_u != A and tmp_u != B:
        ans = min(ans, max(s[shr_u] - x, t[tmp_u] - x))
    if shr_l != -1 and tmp_l != -1:
        ans = min(ans, max(x - s[shr_l], x - t[tmp_l]))
    if shr_l != -1 and tmp_u != B:
        cost = t[tmp_u] - s[shr_l] + min(x - s[shr_l], t[tmp_u] - x)
        ans = min(ans, cost)
    if shr_u != A and tmp_l != -1:
        cost = s[shr_u] - t[tmp_l] + min(s[shr_u] - x, x - t[tmp_l])
        ans = min(ans, cost)
    print(ans)