from heapq import heappop, heappush

N,M=map(int,input().split())
A=list(map(int,input().split()))

B = []
for i in range(N):
  heappush(B,-A[i])

for i in range(M):
  a = heappop(B)
  a /= 2
  heappush(B,a)

print(sum([int(-B[i]) for i in range(N)]))