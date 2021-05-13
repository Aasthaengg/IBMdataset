def resolve():
    A, B, C = list(map(int, input().split()))
    ans = ''
    if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        ans = 0
    else:
        ans = min(B * C, C * A, A * B)

    print(ans)
    return


resolve()