s=input()
k=int(input())
cnt=0
for ss in s:
  if ss=='1':
    cnt+=1
  else:
    break
if cnt==0:
  print(s[0])
  exit()
if k<=cnt:
  print(1)
else:
  print(s[cnt])