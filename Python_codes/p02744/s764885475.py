N = int(input())

alphabets = [chr(ord('a') + x) for x in range(26)]

ans = []


def dfs(d, i_max, S):
    if d == N-1:
        ans.append(S)
        return
    for i in range(i_max+2):
        dfs(d+1, max(i_max, i), S + alphabets[i])


dfs(0, 0, "a")
print(*ans, sep='\n')
