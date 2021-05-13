def resolve():
    N = int(input())
    a = set([N])
    i = 1
    l = 1
    while True:
        i += 1
        if N % 2 == 0:
            N = N // 2
        else:
            N = 3 * N + 1
        a.add(N)
        if l == len(a):
            print(i)
            break
        else:
            l += 1


resolve()
