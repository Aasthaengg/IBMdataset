s='CODEFESTIVAL2016'
res=0
for i,c in enumerate(input()):
  res += c!=s[i]
print(res)