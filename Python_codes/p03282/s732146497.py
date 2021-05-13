s=list(input())
k=int(input())
ch=0
for i in range(len(s)):
  if s[i]=='1':
    ch+=1
  else:
    ss=s[i]
    break
    
if ch>=k:
  print(1)
else:
  print(str(ss))