s=list(map(int,list(input())))
k=int(input())
cnt1=0
for si in s:
  if si==1:
    cnt1+=1
  else:
    break
if k<=cnt1:
  print(1)
else:
  print(s[cnt1])
