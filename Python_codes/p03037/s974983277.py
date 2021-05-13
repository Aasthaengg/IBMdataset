def abc127c():
    n, m = map(int, input().split())
    ls = []
    rs = []
    for _ in range(m):
        l, r = map(int, input().split())
        ls.append(l)
        rs.append(r)
    ans = max(min(rs)-max(ls)+1, 0)
    print(ans)
abc127c()