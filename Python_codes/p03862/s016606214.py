def resolve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = []
    if a[0] <= x:
        ans.append(a[0])
    else:
        ans.append(x)
    for i in range(1,n):
        if ans[i-1] + a[i] <= x:
            ans.append(a[i])
        else:
            ans.append(x-ans[i-1])
    print(sum(a)-sum(ans))

resolve()