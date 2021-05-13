s=str(input())
count=0
for i in range(len(s)):
  if count==0 and s[i]=='C':
    count+=1
  elif count==1 and s[i]=='F':
    count+=1
    print('Yes');exit()
    
print('No')