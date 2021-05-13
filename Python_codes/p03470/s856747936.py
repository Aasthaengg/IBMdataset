def resolve():
    n = int(input())
    dl = list()
    for i in range(n):
        d = int(input())
        dl.append(d)
    dl = sorted(dl, reverse=True)
    pre = 110
    ans = 0
    for d in dl:
        if d < pre:
            ans += 1
        pre = d
    print(ans)
resolve()