from scipy.sparse.csgraph import shortest_path
N, M = map(int, input().split())
dic = [[0]*N for i in range(N)]
Els = []
for i in range(M):
  a, b, c = map(int, input().split())
  dic[a-1][b-1] = c
  dic[b-1][a-1] = c
  Els += [(a-1,b-1,c)]
d, p = shortest_path(dic, return_predecessors=True, method='D')

ans = 0
for a, b, c in Els:
  if p[a][b]!=a:
    ans += 1
print(ans)