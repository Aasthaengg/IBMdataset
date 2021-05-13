s=input()
leng=len(s)
if (leng%2==1):
  print("No")
else:
  check="hi"*(leng//2)
  if (s==check):
    print("Yes")
  else:
    print("No")