import sys
input = sys.stdin.readline
read = sys.stdin.read

import heapq

def main():
  n, q = map(int, input().split())
  event = []
  stop = set()
  minque = []
  for _ in range(n):
    s, t, x = map(int, input().split())
    event.append((s-x, 1, x))
    event.append((t-x, -1, x))
  event.sort()
  event.append((float("inf"), 0, 0))
  D = list(map(int, read().split()))
  now = 0
  for t, b, x in event:
    while minque and minque[0] not in stop:
      heapq.heappop(minque)
    m = minque[0] if minque else -1
    while t > D[now]:
      print(m)
      now += 1
      if now == q:
        exit()
    if b == 1:
      stop.add(x)
      heapq.heappush(minque, x)
    else:
      stop.remove(x)
      
if __name__ == "__main__":
  main()