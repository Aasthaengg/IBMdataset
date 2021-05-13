N=int(input())
s=str(input())
S=list(s)
countr=0
countb=0
for i in range(N):
  if S[i]=='R':
    countr+=1
  else:
    countb+=1
if countr>countb:
  print('Yes')
else:
  print('No')