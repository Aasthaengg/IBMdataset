def abc140c():
    n = int(input())
    b = list(map(int, input().split()))
    ans = 0
    for i in range(len(b)):
        if i == 0:
            ans += b[i]

        if i == n-2:
            ans += b[i]

        if 0 < i :
            ans += min(b[i-1], b[i])
    print(ans)
abc140c()