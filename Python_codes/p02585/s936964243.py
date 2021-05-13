n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
ttl=[]
cnt=[]
count=0
for i in range(n):
  nxt=i+1
  grp=[]
  count=0
  pnt=[]
  pnt.append(0)
  for j in range(n):
    nxt=p[nxt-1]
    pnt.append(pnt[j]+c[nxt-1])
    count+=1
    if nxt==i+1:
      del pnt[0]
      ttl.append(pnt)
      cnt.append(count)
      break
ans=[]
for i in range(n):
  peak=ttl[i].index(max(ttl[i]))
  if k<=cnt[i]:
    ans.append(max(ttl[i][:k]))
  else:
    if ttl[i][-1]<0:
      ans.append(ttl[i][peak])
    else:
      if k%cnt[i]==0:
        ans.append(((k-peak-1)//cnt[i])*ttl[i][-1]+ttl[i][peak])
      else:
        ans.append(max((k//cnt[i])*ttl[i][-1]+max(ttl[i][0:k%cnt[i]]),((k-peak-1)//cnt[i])*ttl[i][-1]+ttl[i][peak]))
print(max(ans))