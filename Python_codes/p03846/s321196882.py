N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
cnt = [0] * N
flag = 1
for i in range(N):
  cnt[A[i]] += 1
if(N % 2 == 1):
  if(cnt[0] != 1):
    flag = 0
  for i in range(1, N):
    if(i%2 == 1 and cnt[i] != 0):
      flag = 0
    elif(i%2 == 0 and cnt[i] != 2):
      flag = 0
else:
  for i in range(N):
    if(i%2 == 1 and cnt[i] != 2):
      flag = 0
    elif(i%2 == 0 and cnt[i] != 0):
      flag = 0
print(flag*pow(2, N//2, mod))