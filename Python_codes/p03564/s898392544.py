n = int(input())
k = int(input())

def dfs(t, i):
    if t == n:
        return i
    return min(dfs(t + 1, i * 2), dfs(t + 1, i  + k))

print(dfs(0, 1))
