import heapq
import math
def main():
  N, H = map(int, input().split())
  A = 0
  B = []
  for i in range(N):
    a, b = map(int, input().split())
    A = max(A, a)
    B.append(-1*b)
  lis = []
  heapq.heapify(B)
  while True:
    temp = -1*heapq.heappop(B)
    if temp > A:
      lis.append(-1*temp)
    if len(B) == 0:
      break
  wa = 0
  ans = 0
  for i in range(len(lis)):
    wa += -1*heapq.heappop(lis)
    ans += 1
    if wa >= H:
      break
  if wa < H:
    ans += math.ceil((H-wa)/A)
  print(ans)
if __name__ == "__main__":
  main()