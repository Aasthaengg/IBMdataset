N, A, B, C = map(int,input().split())
INF = float('inf')
L = []
for _ in range(N):
    L.append(int(input()))

def dfs(i, cnt, a, b, c):
    if i == N:
        if a == 0 or b == 0 or c == 0:
            return INF
        return abs(a - A) + abs(b - B) + abs(c - C) + 10 * cnt
    MP = INF
    if a == 0:
        MP = min(MP, dfs(i+1, cnt, a+L[i], b, c))
    else:
        MP = min(MP, dfs(i+1, cnt+1, a+L[i], b, c))
    if b == 0:
        MP = min(MP, dfs(i+1, cnt, a, b+L[i], c))
    else:
        MP = min(MP, dfs(i+1, cnt+1, a, b+L[i], c))
    if c == 0:
        MP = min(MP, dfs(i+1, cnt, a, b, c+L[i]))
    else:
        MP = min(MP, dfs(i+1, cnt+1, a, b, c+L[i]))
    MP = min(MP, dfs(i+1, cnt, a, b, c))
    
    return MP

print(dfs(0, 0, 0, 0, 0))