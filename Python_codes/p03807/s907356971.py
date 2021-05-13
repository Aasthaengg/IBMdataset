n=int(input())
t=0
A=list(map(int, input().split()))
for i in range(n):
  t+=A[i]
if t%2==0:
  print('YES')
else:
  print('NO')