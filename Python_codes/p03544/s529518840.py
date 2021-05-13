def LucasFib(n, memo={}):
    if n == 0:
        return 2
    if n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = LucasFib(n - 1, memo) + LucasFib(n - 2, memo)
        return memo[n]


def resolve():
    N = int(input())
    print(LucasFib(N))


resolve()
