n=int(input())
a=list(map(int,input().split()))

card=1
cnt=0

for i in a:
  if i==card:
    card+=1
  else:
    cnt+=1

if cnt==n:
  print('-1')

else:
  print(cnt)