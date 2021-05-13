n=int(input())
a=list(map(int,input().split()))
odd=0
even=0
for i in range(n):
  if a[i]%2 == 0:
    even += 1
  else:
    odd += 1
if n == 1:
  print('YES')
elif odd % 2 == 0:
  print('YES')
else:
  print('NO')
