N = int(input())

x = int(N * 100 / 108)

if x * 108 // 100 == N:
  print(x)
elif (x+1) * 108 // 100 == N:
  print(x+1)
else:
  print(':(')