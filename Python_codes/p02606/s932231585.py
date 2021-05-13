L, R, D = map(int, input().split())


def calc(n):
    return n // D


print(calc(R) - calc(L-1))
