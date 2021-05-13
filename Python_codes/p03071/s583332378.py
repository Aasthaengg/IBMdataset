def resolve():
    A, B = map(int, input().split())

    ans = 0
    for _ in [1, 2]:
        if (A <= B):
            ans += B
            B -= 1
        elif (A > B):
            ans += A
            A -= 1

    print(ans)


resolve()