def solve():
    n, x = map(int, input().split())
    s = list(map(int, input().split()))
    cnt, tmp, flg = 0, 0, False
    for i in range(n - 1):
        if i == 0 and s[i] > x:
            cnt += s[i] - x
            s[i] = x
        if s[i] + s[i + 1] > x:
            tmp = s[i] + s[i + 1] - x
            cnt += tmp
            s[i + 1] -= tmp
    print(cnt)



solve()