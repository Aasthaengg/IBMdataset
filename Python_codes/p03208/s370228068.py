def resolve():
    n, k = map(int, input().split())
    H = []
    for _ in range(n):
        H.append(int(input()))
    H_sort = list(sorted(H, reverse=True))
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, H_sort[i]-H_sort[i+k-1])
    print(ans)
resolve()