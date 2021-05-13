s=input()
counter1=0
counter0=0
for i in range(len(s)):
  if s[i]=='0':
    counter0+=1
  else:
    counter1+=1
print(2*min(counter1,counter0))