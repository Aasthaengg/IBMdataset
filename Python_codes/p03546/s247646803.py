H, W = map(int, input().split())
cost = []
INF = 10**9
for i in range(10):
  cost.append(list(map(int, input().split())))
for i in range(10):
  cost[i][i] = INF
A = []
for i in range(H):
  A.append(list(map(int, input().split())))

d = [INF]*10
used = [False] *10
V = 10
def shortest_path(start = 1):#隣接行列の場合のダイクストラ法
  d[start] = 0
  while True:
    v = -1
    for u in range(V):
      if (not used[u]) and (v == -1 or d[u] < d[v]):v = u
    if v == -1:break
    used[v] = True
    for u in range(V):
      d[u] = min(d[u], d[v] + cost[u][v])
  
def main():
  shortest_path()
  ans = 0
  for i in range(H):
    for j in range(W):
      if A[i][j] != -1:
        ans += d[A[i][j]]
  print(ans)
if __name__ == "__main__":
  main()