def solve():
    n = int(input())
    s = list(map(int, input().split()))
    flg = True
    ma = 0
    for ss in s:
        ma = max(ma, ss)
        if ma - 1 > ss:
            flg = False
    print("Yes" if flg else "No")


solve()
