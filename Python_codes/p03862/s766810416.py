def solve():
    N, x = map(int,input().split())
    a = list(map(int,input().split()))

    ans = 0
    for i in range(1,N):
        sm = a[i-1] + a[i]
        if sm - a[i] <= x:
            a[i] -= max(0,sm - x)
            ans += max(0,sm - x)
        else:
            ans += a[i]
            ans += max(0,sm - a[i] - x)
            a[i] = 0

    print(ans)
if __name__ == '__main__':
    solve()
