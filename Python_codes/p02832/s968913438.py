n = int(input())
a = list(map(int,input().split()))
now_number = 0

for i in range(n):
  if a[i] == now_number+1:
    now_number = a[i]

if now_number == 0:
  print(-1)
else:
  print(n - now_number)