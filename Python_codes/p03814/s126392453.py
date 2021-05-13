s=input();i=s[::-1].index("Z");
if i==0:
  i=len(s)
else:
  i=-i
print(len(s[s.index("A"):i]))