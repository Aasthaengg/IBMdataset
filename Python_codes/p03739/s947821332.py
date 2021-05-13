N = int(input())
A = list(map(int,input().split()))

cumsum1 = 0
ans1 = 0

for n in range(N):
  cumsum1 += A[n]
  if n % 2 == 0:
    if cumsum1 >= 0:
      ans1 += abs(cumsum1)+1
      cumsum1 = -1
  else:
    if cumsum1 <= 0:
      ans1 += abs(cumsum1)+1
      cumsum1 = 1
      
      
cumsum2 = 0
ans2 = 0

for n in range(N):
  cumsum2 += A[n]
  if n % 2 == 0:
    if cumsum2 <= 0:
      ans2 += abs(cumsum2)+1
      cumsum2 = 1
  else:
    if cumsum2 >= 0:
      ans2 += abs(cumsum2)+1
      cumsum2 = -1
      
print(min(ans1,ans2))