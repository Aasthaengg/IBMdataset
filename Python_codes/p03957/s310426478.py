s=input()
c=False
f=False
for ch in s:
  if ch=="C":
    c=True
  if c and ch=="F":
    print("Yes")
    break
else:
  print("No")