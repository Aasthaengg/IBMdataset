li=list(input())
lis=li.copy()
count1=0
count2=0
for i in range(0,len(li)):
  if li[i]=='P':
      try:
        if li[i+1]!='P':
          count1+=1
          li[i+1]='D'
      except IndexError:
          continue
  elif li[i]=='?':
      li[i]='P'
  else:
      continue
    
for i in range(0,len(lis)):
  if lis[i]=='P':
      try:
        if lis[i+1]!='P':
          count2+=1
          lis[i+1]='D'
      except IndexError:
          continue
  elif lis[i]=='?':
      lis[i]='D'
    
    
  else:
      continue


c=li.count('D')
d=lis.count('D')
a=c+count1
b=d+count2
if a>=b:
  for i in li:
    print(i,end='')
else:
  for i in lis:
      print(i,end='')

