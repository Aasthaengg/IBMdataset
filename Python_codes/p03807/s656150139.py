N=int(input())
li = list(map(int, input().split()))
if sum(li)%2==0:
  print('YES')
else:
  print('NO')