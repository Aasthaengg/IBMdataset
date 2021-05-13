n, k = list(map(int, input().split()))


def check(p):
    i = 0
    for j in range(k):
        s = 0
        while s + T[i] <= p:
            s += T[i]
            i += 1
            if i == n:
                return n
    return i


def solve():
    left = 0
    right = 100000 * 10000
    while right - left > 1:
        mid = (left + right) // 2
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right


T = []
for _ in range(n):
    T.append(int(input()))
ans = solve()
print(ans)

