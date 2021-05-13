N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A2.reverse()

for i in range(N-1):
  A1[i+1] += A1[i]
  A2[i+1] += A2[i]
  
ans = 0
for i in range(N):
  ans = max(ans, A1[i]+A2[N-1-i])
  
print(ans)
