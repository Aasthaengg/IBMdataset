def solve():
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        s.append(int(input()))
    s.sort()
    res = 10 ** 10
    for i in range(n + 1 - k):
        tmp = s[i + k - 1] - s[i]
        res = min(res, tmp)
    print(res)

solve()