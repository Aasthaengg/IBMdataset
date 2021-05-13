import sys
a=input()
b=input()
for i in reversed(range(len(a)-len(b)+1)):
  t=True
  for j in range(len(b)):
    if not(a[i+j]=="?") and not(a[i+j]==b[j]):
      t=False
      break
  if t:
    for p in range(i):
      if a[p]=="?":
        print("a",end="")
      else:
        print(a[p],end="")
    print(b,end="")
    for w in range(i+len(b),len(a)):
      if a[w]=="?":
        print("a",end="")
      else:
        print(a[w],end="")
    sys.exit()
print("UNRESTORABLE")
