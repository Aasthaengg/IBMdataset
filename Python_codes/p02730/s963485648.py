s = list(input())
if s == list(reversed(s)) and s[:len(s)//2] == list(reversed(s[:len(s)//2])):
  print("Yes")
else:
  print("No")