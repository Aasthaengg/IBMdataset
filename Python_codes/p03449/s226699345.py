N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans = []

for n in range(N):
  ame = 0
  for i in range(n+1):
    ame += A1[i]
  for j in range(n, N):
    ame += A2[j]
  ans.append(ame)
  
print(max(ans))