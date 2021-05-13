def resolve():
    N, M = list(map(int, input().split()))
    base = min(N, M//2)
    if N >= M//2:
        add = 0
    else:
        add = (M - N*2)//4
    print(base+add)

if '__main__' == __name__:
    resolve()