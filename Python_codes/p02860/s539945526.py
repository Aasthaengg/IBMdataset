a = int(input())
b = input()
if b[:int(a/2)] == b[int(a/2):]:
  print("Yes")
else:
  print("No")