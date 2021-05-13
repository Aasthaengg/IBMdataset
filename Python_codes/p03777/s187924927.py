a,b = input().strip().split()

ret = ""
if a == "H":
  ret = b
else:
  if b == "H":
    ret = "D"
  else:
    ret = "H"
print(ret)