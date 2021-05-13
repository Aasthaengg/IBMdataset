def resolve():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    ans = 0
    for z in range(X+1, Y+1):
        if max(x)<z and z<=min(y):
            ans += 1
    print("No War" if ans != 0 else "War")
resolve()