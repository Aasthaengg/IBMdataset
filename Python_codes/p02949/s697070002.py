import sys
input = sys.stdin.readline

def main():
  n, m, p = map(int, input().split())
  edge = []
  for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((a, b, p-c))
  dist = [float("inf")]*(n+1)
  dist[1] = 0
  for i in range(n):
    for a, b, c in edge:
      if dist[b] > dist[a] + c:
        dist[b] = dist[a] + c
  ans = min(dist[n], 0)
  for i in range(n):
    for a, b, c in edge:
      if dist[b] != -float("inf") and dist[b] > dist[a] + c:
        dist[b] = -float("inf")
  if dist[n] == -float("inf"):
    ans = 1
  print(-ans)
if __name__ == "__main__":
  main()