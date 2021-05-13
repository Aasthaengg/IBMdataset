N = int(input())
arr = list(map(int, input().strip().split()))
ans = 0

for i in range(0,N):
  for j in range(i+1,N):
    ans = ans + arr[i]*arr[j]
print (ans)