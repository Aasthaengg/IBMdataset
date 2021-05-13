s=input()
count=0
for i in range(len(s)):
  if(i%2==0 and s[i]=='g'):
    count=count
  if(i%2==0 and s[i]=='p'):
    count=count-1
  if(i%2==1 and s[i]=='g'):
    count=count+1
  if(i%2==1 and s[i]=='p'):
    count=count

print(count)