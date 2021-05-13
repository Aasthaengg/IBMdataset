_input = input().split(" ")
_A = int(_input[0])
_B = int(_input[1])

if _A + _B < 24:
  print(_A + _B)
else:
  print(_A + _B - 24)