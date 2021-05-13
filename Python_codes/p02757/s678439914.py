# fin=open('in','r')
# input=lambda:fin.readline().strip()
n,p=map(int,input().split())
s=list(map(int,input()))
if p==2 or p==5:
  r=0
  for i in range(n):
    if s[i]%p==0:
      r+=i+1
  print(r)
else:
  c=0
  cnt=[0]*p
  cnt[0]+=1
  for k in range(len(s)-1,-1,-1):
      c=(c+s[k]*pow(10,len(s)-1-k,p))%p
      cnt[c]+=1
  print(sum(x*(x-1)//2 for x in cnt))