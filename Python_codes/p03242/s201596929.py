n=input()
s=''

for i in n:
  if i=="1":
    s+='9'
    
  else:
    s+='1'
    
print(''.join(s))