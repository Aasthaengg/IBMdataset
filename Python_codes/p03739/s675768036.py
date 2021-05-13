def solve(x):
    if x == 0:
        return INF

    sgn = (-1) ** (x < 0)
    ret = abs(a[0] - x)
    sm = x
    for e in a[1:]:
        sgn *= -1

        if sgn < 0:
            if sm + e < 0:
                sm += e
            else:
                ret += e + 1 + sm
                sm = -1

        else:
            if sm + e > 0:
                sm += e
            else:
                ret -= e - 1 + sm
                sm = 1

    return ret


n = int(input())
a = list(map(int, input().split()))
INF = 10 ** 18

ans = min(solve(1), solve(-1), solve(a[0]))
print(ans)
