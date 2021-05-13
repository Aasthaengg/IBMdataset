from heapq import heapify, heappop, heappush

def resolve():
  N, M = map(int, input().split(" "))
  A = [(-1)*int(x) for x in input().split(" ")]
  heapify(A)

  for _ in range(M):
    max_A = (-1)*heappop(A)
    heappush(A, (-1)*(max_A//2))
  
  print((-1)*sum(A))

if __name__ == "__main__":
  resolve()