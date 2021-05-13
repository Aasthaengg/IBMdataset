def resolve():
    n, k = map(int, input().split())
    length = list(map(int, input().split()))
    list.sort(length, reverse=True)

    ans = 0
    for i in range(k):
        ans += length[i]
    print(ans)
resolve()