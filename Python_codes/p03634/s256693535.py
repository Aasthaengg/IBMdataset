import sys
sys.setrecursionlimit(10**8)
N = int(input())
a = [[] for i in range(N)]
for i in range(N-1):
  A, B, C = map(int, input().split())
  a[A-1].append([B-1, C])
  a[B-1].append([A-1, C])
dist = [-1]*N
Q, K = map(int, input().split())
dist[K-1] = 0

def dfs(now):
  for i, dis_e in a[now]:
    if dist[i] == -1:
      dist[i] = dist[now] + dis_e
      dfs(i)

def main():
  dfs(K-1)
  ans = []
  for i in range(Q):
    x, y = map(int, input().split())
    ans.append(dist[x-1]+dist[y-1])
  print(*ans, sep = "\n")

if __name__ == "__main__":
  main()