N,M=map(int,input().split())
road=[list(map(int,input().split())) for _ in range(M)]
result={i:0 for i in range(1, N+1)}
for i,j in road:
  result[i] += 1
  result[j] += 1
[print(result[i]) for i in range(1, N+1)]