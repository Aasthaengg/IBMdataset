def resolve():
    N = int(input())
    P = list(map(int, input().split()))
    tmpmin = float("inf")
    ans = 0
    for p in P:
        if tmpmin > p:
            ans += 1
        tmpmin = min(tmpmin, p)
    print(ans)

if '__main__' == __name__:
    resolve()