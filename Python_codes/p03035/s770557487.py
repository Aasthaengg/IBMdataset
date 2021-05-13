x, y = input("").split(" ")
a = int(x)
b = int(y)
result = 0
if a >= 13:
  result = b
elif a >= 6 and a <= 12:
  result = b//2
else:
  result = 0
print(result)