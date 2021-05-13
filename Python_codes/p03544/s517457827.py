def lucas(n, memo={}):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = lucas(n - 1, memo) + lucas(n - 2, memo)
        return lucas(n - 1) + lucas(n - 2)


n = int(input())
print(lucas(n))
