a, b = input().split()
a_str = a * int(b)
b_str = b * int(a)

if a_str < b_str:
  print(a_str)
else:
  print(b_str)
