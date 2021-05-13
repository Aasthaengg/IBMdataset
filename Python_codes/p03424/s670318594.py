n = int(input())
a = list(map(str,input().split()))
ans = 0
for i in range(n):
  if a[i] == 'Y':
    ans +=1
if ans > 0:
  print('Four')
else:
  print('Three')