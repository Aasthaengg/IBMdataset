a = list(map(int, input().split()))
sum = a[0] + a[1]
if sum%2 == 0:
  print(int(sum/2))
else:
  print(int((sum + 1)/2))
