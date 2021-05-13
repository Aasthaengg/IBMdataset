def resolve():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        ca, ta = map(int, input().split())
        c.append(ca)
        t.append(ta)
    ans = []
    for i in range(N):
        if t[i] <= T:
            ans.append(c[i])
    if len(ans) != 0:
        print(c[c.index(min(ans))])
    else:
        print("TLE")
resolve()