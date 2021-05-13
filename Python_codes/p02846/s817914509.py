def solve():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    if A1 < B1 and A2 < B2:
        return 0
    elif A1 > B1 and A2 > B2:
        return 0

    C1, C2 = B1-A1, B2-A2

    if C1 < 0:
        C1, C2 = -C1, -C2

    dist = C1*T1 + C2*T2
    if dist == 0:
        return 'infinity'
    elif dist > 0:
        return 0

    diff = C1*T1
    num = diff // abs(dist) * 2

    if diff % abs(dist):
        num += 1

    return num


print(solve())
