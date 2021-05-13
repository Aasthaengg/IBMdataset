def resolve():
    N, M = list(map(int, input().split()))
    l = []
    ls = list(range(1, M+1))

    for i in range(N):
        l = list(map(int, input().split()))
        ls = set(l[1:]).intersection(ls)
    print(len(ls))
    return

resolve()