def resolve():
    D, N = list(map(int, input().split()))
    ls = [100 ** D * i for i in range(1, 100)]
    ls.append(100 ** D * 101)
    print(ls[N-1])
    return

resolve()