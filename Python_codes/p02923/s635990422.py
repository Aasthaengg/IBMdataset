def solve():
    n = int(input())
    s = list(map(int, input().split()))
    tmp = 0
    res = 0
    for a, b in zip(s, s[1:]):
        if a >= b:
            tmp += 1
            res = max(res, tmp)
        else:
            tmp = 0
    print(res)


solve()
