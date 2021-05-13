n = int(input())
k = len(set(map(str, input().split())))
if k == 4:
  print('Four')
else:
  print('Three')