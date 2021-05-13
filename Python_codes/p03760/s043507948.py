o=input()
e=input()
pw=""
for i in range(len(o)+len(e)):
  if i%2==0:
    pw=pw+o[i//2]
  else:
    pw=pw+e[i//2]
print(pw)