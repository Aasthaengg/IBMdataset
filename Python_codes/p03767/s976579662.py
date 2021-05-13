def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    s_a = sorted(A, reverse=True)[:2*n]
    ans = 0
    for i in range(0, 2*n, 2):
        ans += s_a[i+1]
    print(ans)
resolve()