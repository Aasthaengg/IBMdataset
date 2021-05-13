def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(int(input()))
    s.sort()
    res = 0
    for i, x in enumerate(s):
        res += x
        if i == n - 1:
            res -= x // 2
    print(res)

solve()