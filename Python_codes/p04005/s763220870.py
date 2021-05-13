A = list(map(int, input().split()))

newlist = sorted(A, reverse=True)
if newlist[0]%2 == 0:
  print('0')
else:
  print(newlist[1]*newlist[2])
