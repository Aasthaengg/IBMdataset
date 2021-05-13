N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
INF = 10**9

def dfs(cur, a, b, c):
  if cur == N:
    return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a,b,c)>0 else INF

  ans = INF
  ans = min(ans, dfs(cur+1, a, b, c))
  ans = min(ans, dfs(cur+1, a + l[cur], b, c)+10)
  ans = min(ans, dfs(cur+1, a, b+l[cur], c)+10)
  ans = min(ans, dfs(cur+1, a, b, c+l[cur])+10)
  return ans

print(dfs(0, 0, 0, 0))
