S=input()
cnt=0
for c in S:
   cnt+=c=='o'
if cnt+15-len(S)>=8:
   print('YES')
else:
  print('NO')
