s=input()
t=''
while s!='':
  if len(s)<=4:
    break
  elif s[:5]=='dream':
    if len(s)>=10 and s[5:10]=='erase':
      s=s[5:]
      continue
    elif len(s)>=7 and s[5:7]=='er':
      s=s[7:]
      continue
    else:
      s=s[5:]
      continue
  elif s[:5]=='erase':
    if len(s)>=6 and s[5]=='r':
      s=s[6:]
      continue
    else:
      s=s[5:]
      continue
  
  elif s[:5]!='dream' and s[:5]!='erase':
    break
      
    
if s=='':
  print('YES')
  
else:
  print('NO')