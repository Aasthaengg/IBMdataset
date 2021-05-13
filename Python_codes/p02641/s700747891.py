def resolve():
    X, N = list(map(int, input().split()))
    P = list(map(int, input().split()))
    ans = float("inf")
    for i in range(0, 102):
        if i in P:
            continue
        if abs(X-ans) > abs(X-i):
            ans = i
        elif abs(X-ans) == abs(X-i):
            ans = min(ans, i)
    print(ans)


if '__main__' == __name__:
    resolve()