import heapq as hq
N,M=list(map(int, input().split()))
A=list(map(int, input().split()))
B=[(-1)*A[i] for i in range(N)]
B.sort()
for _ in range(M):
  a=hq.heappop(B)
  a=((a*(-1))//2)*(-1)
  hq.heappush(B,a)
C=[-B[i] for i in range(N)]
print(sum(C))