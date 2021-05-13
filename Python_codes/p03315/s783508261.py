s=input()
plus=0
minus=0
for i in range(4):
  if s[i]=='+':
    plus+=1
  else:
    minus+=1
print(plus-minus)