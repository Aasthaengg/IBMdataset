A=input()
cntg=0
cntp=0
cnt=0
for i in A:
  if i=='g':
    if cntg==cntp:
      cntg+=1
    else:
      cntp+=1
      cnt+=1
  else:
    if cntg==cntp:
      cntg+=1
      cnt-=1
    else:
      cntp+=1
print(cnt)