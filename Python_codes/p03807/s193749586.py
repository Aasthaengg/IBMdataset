n = int(input())
A = list(map(int,input().split()))

count_odd = sum([a%2==1 for a in A])
if count_odd%2==1 and count_odd>=1:
  print('NO')
else:
  print('YES')