s=input()
for i in range(2,len(s)+1,2):
  if s[:(len(s)-i)//2]==s[(len(s)-i)//2:len(s)-i]:
    print(len(s)-i)
    exit()
if s[0]==s[1]:
  print(2)