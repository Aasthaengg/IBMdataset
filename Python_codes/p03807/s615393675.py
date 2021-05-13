N=int(input())
A=[x for x in list(map(int,input().split())) if x%2!=0]

if len(A)%2==0:
  print('YES')
else:
  print('NO')