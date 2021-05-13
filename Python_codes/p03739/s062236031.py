from itertools import accumulate


def solve(condition):
    sub, add = 0, 0
    for i in range(N):
        cur = acc[i] + add - sub
        if i % 2 == condition:
            if cur > 0:
                continue
            add += 1 - cur
        else:
            if cur < 0:
                continue
            sub += cur + 1
    return sub + add


N, *A = map(int, open(0).read().split())
acc = list(accumulate(A))
ans = min(solve(0), solve(1))
print(ans)
