s=input()
st=200000
for i in range(len(s)):
  if s[i]=="A" and st>i:
    st=i
  elif s[i]=="Z":
    en=i
print(en-st+1)