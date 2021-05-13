def resolve():
    A, B, C = list(map(int, input().split()))
    if (A % 2 == 0 and B % 2 == 0 and C % 2 == 0):
        if (A == B and B == C and C == A):
            print(-1)
            return

    if (A % 2 == 1 or B % 2 == 1 or C % 2 == 1):
        print(0)
        return

    ans = 0
    while True:
        A, B, C = (B / 2 + C / 2), (C / 2 + A / 2), (A / 2 + B / 2)
        ans += 1
        if (A % 2 == 1 or B % 2 == 1 or C % 2 == 1):
            print(ans)
            return

    return


resolve()
