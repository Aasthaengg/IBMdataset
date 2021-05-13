s="CODEFESTIVAL2016"
t=input()
a=0
for i in range(16):
  if not(s[i]==t[i]):
    a+=1
print(a)