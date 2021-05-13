import math
n = int(input())
A = [int(i) for i in input().split()]
cnt, ans = 0, 0
for i in range(n-1):
  if A[i] == A[i+1]:
    cnt += 1
    if i == n-2:
      ans += math.floor((cnt+1)/2)
  else:
    ans += math.floor((cnt+1)/2)
    cnt = 0
print(ans)