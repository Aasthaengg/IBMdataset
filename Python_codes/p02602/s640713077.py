# 解説

def main():
    from math import log10

    N, K = map(int, input().split())
    *A, = map(int, input().split())

    def accumulate(a):
        s = 0
        for x in a:
            s += log10(x)
            yield s

    *acc, = accumulate(A)
    for i in range(N - 1, K - 1, -1):
        acc[i] -= acc[i - K]

    for i in range(K, N):
        if acc[i] > acc[i - 1] + 1e-10:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
