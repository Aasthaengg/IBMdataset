n,m=map(int,input().split())
lst=[list(input().split()) for i in range(m)]
x,y=0,0
cnt=['?']+[0]*n
cnt2=[0]+[0]*n
for i in lst:
  if i[1]=='WA':
    pin=int(i[0])
    if cnt[pin]!='AC':
      cnt2[pin]+=1
  elif i[1]=='AC':
    cnt[int(i[0])]='AC'

x=cnt.count('AC')

for i in range(len(cnt)):
  if cnt[i]=='AC':
    y+=cnt2[i]
print(x,y)