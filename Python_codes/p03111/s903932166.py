N,A,B,C = map(int, input().split())
l = list(int(input()) for _ in range(N))
inf = 10 ** 9
def dfs(cur,a,b,c):
    if cur == N:
        return abs(a-A) + abs(b-B) + abs(c-C) -30 if min(a,b,c) > 0 else inf
    re0 = dfs(cur+1, a, b, c)
    re1 = dfs(cur+1, a+l[cur], b, c)+10
    re2 = dfs(cur+1, a, b+l[cur], c) + 10
    re3 = dfs(cur+1, a, b, c+l[cur]) + 10
    return min (re0, re1, re2, re3)
print(dfs(0,0,0,0))
