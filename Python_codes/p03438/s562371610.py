n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = sum(b) - sum(a)
cnt = 0
for i in range(n):
  if b[i] < a[i]:
    cnt += a[i] - b[i]
  elif (b[i] + a[i]) % 2 == 1:
    cnt += 1
if cnt <= k:
  print('Yes')
else:
  print('No')