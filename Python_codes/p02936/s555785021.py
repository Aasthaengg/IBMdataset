import sys
sys.setrecursionlimit(200000000)
n,q = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
ans=[0]*(n+1)
reached=[0]*(n+1)
def main():
  for i in range(n-1):
    a,b = map(int, input().split())
    graph1[a].append(b)
    graph2[b].append(a)

  for i in range(q):
    p,x = map(int, input().split())
    ans[p] += x
  dfs(1) 
  print(' '.join([str(i) for i in ans[1:]]))

def dfs(i):
  if reached[i] == 1:
    return
  reached[i] = 1
  for g in graph1[i], graph2[i]:
    for j in g:
      if reached[j] == 1:
        continue
      ans[j] += ans[i]
      dfs(j)

if __name__ == '__main__':
  main()