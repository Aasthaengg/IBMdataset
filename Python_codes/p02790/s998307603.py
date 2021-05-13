a, b = input().split(" ")
if int(a) > int(b):
  print("".join([b] * int(a)))
else:
  print("".join([a] * int(b)))