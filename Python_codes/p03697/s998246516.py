A = list(map(int, input().split()))

if sum(A) >= 10:
  print('error')
else:
  print(sum(A))