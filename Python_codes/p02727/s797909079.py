import heapq
X, Y, A, B, C = map(int, input().split())
AL = list(map(int, input().split()))
BL = list(map(int, input().split()))
CL = list(map(int, input().split()))
h = []
for a in AL:
  heapq.heappush(h, (-a, 0))
for b in BL:
  heapq.heappush(h, (-b, 1))
for c in CL:
  heapq.heappush(h, (-c, 2))
answer = 0
x_cnt = 0
y_cnt = 0
eat_cnt = 0
for _ in range(A+B+C):
  if eat_cnt >= X+Y:
    break
  d, t = heapq.heappop(h)
  if t == 0 and x_cnt+1 <= X:
    answer += -d
    x_cnt += 1
    eat_cnt += 1
  elif t == 1 and y_cnt+1 <= Y:
    answer += -d
    y_cnt += 1
    eat_cnt += 1
  elif t == 2:
    answer += -d
    eat_cnt += 1
print(answer)