N, Y = map(int, input().split())
m = 10000,5000,1000
ans = -1,-1,-1
for i in range(N+1):
  for j in range(N-i+1):
    k = N-i-j
    if Y==m[0]*i+m[1]*j+m[2]*k:
      ans = i,j,k
      break
      
print(*ans)