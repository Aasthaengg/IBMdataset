a=input()
b=input()
if len(a)+1==len(b) and b[:len(a)]==a:
  print("Yes")
else:
  print("No")