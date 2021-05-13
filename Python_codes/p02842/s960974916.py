def resolve():
    N = int(input())
    a = int(N // 1.08)
    if int(a * 1.08) == N:
        print(a)
    elif int((a + 1) * 1.08) == N:
        print(a + 1)
    else:
        print(":(")
resolve()