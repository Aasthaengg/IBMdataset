N = int(input())

resultA = N * 100 // 108
resultB = resultA + 1
valueA = resultA * 108 // 100
valueB = resultB * 108 // 100

if N == valueA:
  print(resultA)
elif N == valueB:
  print(resultB)
else:
  print(':(')