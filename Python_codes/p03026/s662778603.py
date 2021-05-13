import collections
import sys
input = sys.stdin.readline
import heapq
def solve():
  n = int(input())

  query2 = []
  edge = [[] for _ in range(n)]
  ans = [ 0 for i in range(n)]
  for i in range(n-1):
    a,b = (int(i) for i in input().split())
    query2.append(a)
    query2.append(b)
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
  c = list(int(i) for i in input().split())
  if n == 1:
    print(0)
    print(c[0])
    exit()
  c = collections.deque(sorted(c,reverse =True))
  d = collections.Counter(query2)
  d2 = d.most_common()
  bfs = []
  heapq.heappush(bfs,(-1*d2[0][1],d2[0][0]-1))#回数,場所、親
  ct = 0
  visit = [False]*n
  
  while bfs:
    times,place = heapq.heappop(bfs)
    if visit[place]:
      continue
    else:
      visit[place] = True

      for i in range(len(edge[place])):
        newp = edge[place][i]
        newtimes = len(edge[newp])
        if not visit[newp]:
          heapq.heappush(bfs,(-1*newtimes,newp))
      #print(place,parent,times)
      ans[place] = c.popleft()

      #print(c,place)

  print(sum(ans)-max(ans))
  print(*ans)
  
solve()
