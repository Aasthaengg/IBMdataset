n=int(input())
a=list(map(int,input().split()))
cnt1=0
cnt2=0
cnt4=0
for i in a:
  if i%2==1:
    cnt1+=1
  elif i%4!=0:
    cnt2+=1
  elif i%4==0:
    cnt4+=1
if cnt2==0:
  if cnt1<=cnt4+1:
    print('Yes')
  else:
    print('No')
else:
  if cnt1<=cnt4:
    print('Yes')
  else:
    print('No')