n,k=list(map(int,input().split()))
s=input()
cnt=[[],[]]
st=1
c=0
for i in s:
  if st==int(i):
    c+=1
  else:
    cnt[st].append(c)
    c=1
    st=1-st
cnt[st].append(c)
cnt[0].append(0)
cnt[1].append(0)
sm=[[],[]]
s=0
for i in cnt[0]:
  s+=i
  sm[0].append(s)
s=0
for i in cnt[1]:
  s+=i
  sm[1].append(s)
sm[0][-1]=0
sm[1][-1]=0
if len(cnt[0])<=k+1:
  print(n)
else:
  m=0
  for i in range(len(cnt[0])-k):
    s=sm[0][i+k-1]-sm[0][i-1]+sm[1][min(i+k,len(cnt[1])-2)]-sm[1][i-1]
    m=max(s,m)
  print(m)