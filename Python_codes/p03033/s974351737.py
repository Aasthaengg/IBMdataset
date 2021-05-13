import heapq
def main():
  N, Q = list(map(int, input().split()))
  STX = tuple(list(map(int, input().split())) for _ in range(N))
  D = tuple([int(input()) for _ in range(Q)])

  L = []
  for s, t, x in STX:
    L.append((x, s - x, t - x))

  L.sort(key = lambda x: x[1])
  q = []
  cnt = 0
  push = heapq.heappush
  pop = heapq.heappop
  t = []
  for i in range(Q):
    while cnt < len(L) and D[i] >= L[cnt][1]:
      if t != []:
        push(q, t)
        t = []
      push(q, L[cnt])
      cnt += 1
    if t != [] and t[2] > D[i]:
      print(t[0])
    else:
      while q != []:
        t = pop(q)
        if t[2] > D[i]:
          print(t[0])
          break
      else:
        t = []
        print(-1)

main()
