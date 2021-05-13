def actual(S, W):
    if W >= S:
        return 'unsafe'

    return 'safe'

S, W = map(int, input().split())

print(actual(S, W))