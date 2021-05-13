s = input()
lis = list(s)

if lis[0] == lis[1] or lis[1] == lis[2] or lis[2] == lis[3]:
  print("Bad")
else:
  print("Good")