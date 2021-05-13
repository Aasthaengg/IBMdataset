N, M = map(int,input().split())


def calculate(n, m):

    if (m // 2) < n:
        print(m // 2)
        return

    res = ((m - n * 2) // 4) + n
    print(res)

calculate(N, M)

