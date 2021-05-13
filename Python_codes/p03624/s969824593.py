s = input()
s = set(s)
abc = "abcdefghijklmnopqrstuvwxyz"
for i in abc:
  if i not in s:
    print(i)
    break
else:
  print("None")