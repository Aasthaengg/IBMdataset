x = int(input())
i = 1
val = x
while val % 360 != 0:
  val += x
  i += 1
print(i)