n = int(input())
a = list(map(int,input().split()))

b = list(map(lambda x : x%2 , a))
if sum(b)%2 :
  print('NO')
else:
  print('YES')