def resolve():
    n, m, x = map(int, input().split())
    al = list(map(int, input().split()))
    al = sorted(al)
    ans = [0, 0]
    for i in al:
        if i < x:
            ans[0] += 1
        elif x < i:
            ans[1] += 1
    ans = sorted(ans)
    print(ans[0])
resolve()