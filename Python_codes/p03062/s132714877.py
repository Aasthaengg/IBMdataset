N = int(input())
A = list(map(int, input().split()))
INF = 10**20

DP = [[0 for _ in range(2)] for _ in range(N)]
DP[0][1] = -INF

for i in range(1,N): 
  DP[i][0] = max(DP[i-1][0] + A[i-1], DP[i-1][1] - A[i-1])
  DP[i][1] = max(DP[i-1][1] + A[i-1], DP[i-1][0] - A[i-1])
  #print(i,DP[i])
  
print(max(DP[N-1][0]+A[N-1], DP[N-1][1]-A[N-1]))