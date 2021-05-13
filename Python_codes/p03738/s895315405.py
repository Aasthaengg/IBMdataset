a=input()
b=input()
x=max(len(a),len(b))
a=format(a).zfill(x)
b=format(b).zfill(x)
if a>b:
  print("GREATER")
elif a<b:
  print("LESS")
else:
  print("EQUAL")