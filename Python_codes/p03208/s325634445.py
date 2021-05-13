def resolve():
    n, k = map(int, input().split())
    H_sort = list(sorted([int(input()) for _ in range(n)],reverse=True))
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, H_sort[i]-H_sort[i+k-1])
    print(ans)
resolve()