def check(P, k, n, T):
    res = 0
    for _ in range(k):
        s = 0
        while s + T[res] <= P:
            s += T[res]
            res += 1
            if res == n:
                return n
    return res

n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

left = 0
right = n * 10000
mid = (left + right) // 2
while right - left > 1:
    v = check(mid, k, n, w)
    if v == n:
        right = mid
    else:
        left = mid
    mid = (left + right) // 2
print(right)
