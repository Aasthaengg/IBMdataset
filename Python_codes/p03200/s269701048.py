s = input()
opcount = 0
wcount = 0
bcount = 0
for i in range(len(s)):
  if s[i] == "B":
    bcount += 1
  else:
    if bcount>0:
      opcount += i-wcount
      wcount += 1
    else:
      wcount += 1
print(opcount)