def resolve():
    N, M = map(int, input().split())
    ans = []
    for _ in range(M):
        a, b = map(int, input().split())
        ans.append(a)
        ans.append(b)
    for i in range(1, N+1):
        print(ans.count(i))
resolve()