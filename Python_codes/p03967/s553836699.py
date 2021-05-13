s=input()
counter=0
for i in range(len(s)):
  if s[i]=='p':
    counter+=1
print(len(s)//2-counter)
