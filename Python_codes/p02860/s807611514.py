N = int(input())
str = input()
if len(str) % 2 != 0:
  print("No")
elif str[:int(len(str)/2)] != str[int(len(str)/2):]:
  print("No")
else:
  print("Yes")