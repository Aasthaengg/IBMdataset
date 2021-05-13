n = int(input())
alp = "abcdefghijklmnopqrstuvwxyz"
ans = []


def dfs(s):
    if len(s) == n:
        ans.append(s)
        return 0
    se = len(set(s))
    for i in range(se+1):
        dfs(s+alp[i])


dfs('a')
print(*ans, sep='\n')
