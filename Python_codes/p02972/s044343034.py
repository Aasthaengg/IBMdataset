n = int(input())
a = list(map(int, input().split()))

b =[0]*(n+1)

ans = 0

for i in range(n):
  j = n-i
  sum = 0
  m = 1
  while j*m <= n:
    sum += b[j*m]
    m += 1
  if sum % 2 != a[j-1]:
    b[j] = 1 
    ans += 1
    


if not 1 in b:
  print(0)
else:
  print(ans)
  for i in range(n+1):
    if b[i] == 1:
      print(i, end =' ')
