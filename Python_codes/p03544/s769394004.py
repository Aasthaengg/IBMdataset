N = int(input())

def ryuca_memo(n):
    memo = [0]*(n+1)
    def _ryuca(n):
        if n == 1:
            return 1
        elif n == 0:
            return 2
        if memo[n] != 0:
            return memo[n]
        memo[n] = _ryuca(n-1) + _ryuca(n-2)
        return memo[n]
    return _ryuca(n)

print(ryuca_memo(N))
