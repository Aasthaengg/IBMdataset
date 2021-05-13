def resolve():
    X, Y = map(int, input().split())
    print("-1" if X%Y == 0 else X*(Y-1))
resolve()