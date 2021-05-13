n = int(input())
a = list(map(int, input().split()))


def solve(tmp):
    ans = 0
    for i in range(1, n):
        if tmp * (tmp + a[i]) < 0:
            tmp += a[i]
        else:
            ans += abs(tmp + a[i]) + 1
            if tmp < 0:
                tmp = 1
            else:
                tmp = - 1
    return ans

minus = min(a[0], -1)
plus = max(a[0], 1)
ans = min(solve(plus) + abs(a[0] - plus), solve(minus) + abs(a[0] - minus))
print(ans)
