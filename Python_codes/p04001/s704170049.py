s = input()
n = len(s)

def dfs(i: int, t: str):
    if i == n - 1:
        return sum(list(map(int, t.split('+'))))
    return dfs(i + 1, t + s[i + 1]) + dfs(i + 1, t + '+' + s[i + 1])

print(dfs(0, s[0]))