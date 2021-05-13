s = str(input().rstrip())
l=0
r=1
tmp =''
li = list()
while(r<=len(s)):
  if(s[l:r]!=tmp):
    li.append(s[l:r])
    tmp=s[l:r]
    l=r
    r+=1      
  else:
    r+=1

print(len(li))