N = int(input())

def dfs(x):
    memo = [0]*(x+1)
    def _dfs(x):
        if x == 0:
            return 2
        elif x == 1:
            return 1
        elif memo[x] != 0:
            return memo[x]
        else:
            memo[x] = _dfs(x-1) + _dfs(x-2)
            return memo[x]
    return _dfs(x)

print(dfs(N))