s = list(input().split())
keep =[]
for i in range(len(s)):
  if s[i] == "+":
    keep.append(keep[-1]+keep[-2])
    del keep[-3:-1]
  elif s[i] == "-":
    keep.append(keep[-2]-keep[-1])
    del keep[-3:-1]
  elif s[i] == "*":
    keep.append(keep[-2]*keep[-1])
    del keep[-3:-1]
  elif s[i] == "/":
    keep.append(keep[-2]/keep[-1])
    del keep[-3:-1]
  else:
    keep.append(int(s[i]))
print(keep[-1])
