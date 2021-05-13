s=input()
a=ord("a")
for i in range(26):
  if chr(a+i) in s:
    pass
  else:
    print(chr(a+i))
    break
else:
  print("None")