s = input()
if len(s)%2 == 0:
  for i in range(len(s)//2):
    if s[2*i] != "h" or s[2*i+1] != "i":
      print("No")
      exit()
  print("Yes")
else:
  print("No")