import heapq

def solve():
  k, t = list(map(int, input().split()))
  a = list(map(int, input().split()))
  
  q = []
  
  for i in range(len(a)):
    if a[i] != 0:
      heapq.heappush(q, (-a[i], i))
  
  count, i = heapq.heappop(q)
  count += 1
  keep = (count, i)

  while len(q) > 0:
    count, i = heapq.heappop(q)
    count += 1
    
    if keep[0] < 0:
      heapq.heappush(q, keep)
    keep = (count, i)
  
  print(- keep[0])
  return

if __name__ == "__main__":
  solve()