x=sorted(list(input()))
y=sorted(list(input()),reverse=True)
a=""
b=""
for p in x:
  a+=p
for q in y:
  b+=q
if a<b:
  print("Yes")
else:
  print("No")
