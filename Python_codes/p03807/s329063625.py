N = int(input())
A = list(map(int, input().split()))
odd = [x%2!=0 for x in A].count(True)
if odd%2 == 0:
  print('YES')
else:
  print('NO')