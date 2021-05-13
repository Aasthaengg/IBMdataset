N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
result = 0

for i in range(N):
  d = V[i]-C[i]
  if d>=0:
    result += d
  else:
    result += 0
    
print(result)