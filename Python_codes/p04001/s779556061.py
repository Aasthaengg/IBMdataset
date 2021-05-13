S = input()

def dfs(i, f):
    if i == N-1:
        return sum(map(int, f.split('+')))
    return dfs(i+1, f + S[i+1]) + dfs(i+1, f+'+'+S[i+1])

N = len(S)
print(dfs(0, S[0]))
