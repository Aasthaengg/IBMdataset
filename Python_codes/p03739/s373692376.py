N = int(input())
A = list(map(int, input().split()))

count1 = 0
now = A[0]
if now <= 0:
  count1 += (1-A[0])
  now = 1
for i in range(1, N):
  if i%2 == 0:
    if now+A[i] <= 0:
      count1 += 1-(now+A[i])
      now = 1
    else:
      now += A[i]
  else:
    if now+A[i] >= 0:
      count1 += 1+(now+A[i])
      now = -1
    else:
      now += A[i]
      
count2 = 0
now = A[0]
if now >= 0:
  count2 += (1+A[0])
  now = -1
for i in range(1, N):
  if i%2 == 1:
    if now+A[i] <= 0:
      count2 += 1-(now+A[i])
      now = 1
    else:
      now += A[i]
  else:
    if now+A[i] >= 0:
      count2 += 1+(now+A[i])
      now = -1
    else:
      now += A[i]
      
print(min(count1, count2))