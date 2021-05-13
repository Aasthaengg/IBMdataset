a=input()
b=input()
if len(a)==len(b):
  if a>b:
    print("GREATER")
  elif a<b:
    print("LESS")
  else :
    print("EQUAL")
else :
  if len(a)>len(b):
    print("GREATER")
  else:
    print("LESS")