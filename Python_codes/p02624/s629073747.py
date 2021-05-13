N = int(input())

MAX_N = 10000000

Y = []
for j in range(1,N+1):
  Y.append(N//j)

ans = 0
for j in range(1,N+1):
  ans += (j)*Y[j-1]*(Y[j-1]+1)//2


print(ans)