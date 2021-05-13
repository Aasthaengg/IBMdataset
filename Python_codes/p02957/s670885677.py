a, b = [int(i) for i in input("").split(" ")]
if a%2 != b%2:
  print('IMPOSSIBLE')
else:
  print(int((a+b)/2))