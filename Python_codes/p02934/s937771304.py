def solve():
    n = int(input())
    s = list(map(int, input().split()))
    res = 0
    for ss in s:
        res += 1 / ss
    print(1/res)


solve()
