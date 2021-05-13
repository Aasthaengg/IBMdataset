A,B,C,D = (int(x) for x in input().split())

first = A*B
second = C*D

if first >= second:
  print(first)
else:
  print(second)