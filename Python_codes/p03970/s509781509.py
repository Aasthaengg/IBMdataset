s=input()
x='CODEFESTIVAL2016'
c=0
for i in range(16):
  if s[i]!=x[i]:c+=1
print(c)