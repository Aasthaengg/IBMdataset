def comb(n,r):
  ret=1
  for i in range(n,n-r,-1):
    ret=ret*i
  for i in range(2,r+1):
    ret=ret//i
  return ret

n,a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr=sorted(arr,reverse=True)
cnt=[0]*50
num=[arr[0]]
tmp=arr[0]
pos=0
for i in arr:
  if i==tmp:
    cnt[pos]+=1
  else:
    pos+=1
    cnt[pos]+=1
    tmp=i
    num.append(i)
ave=0
ans=0
if cnt[0]>=a:
  ave=num[0]
  for i in range(a,min(b,cnt[0])+1):
    ans+=comb(cnt[0],i)
else:
  t=0
  pos=0
  for i in range(n):
    t+=cnt[i]
    ave+=num[i]*cnt[i]
    if t>=a:
      ave-=num[i]*(t-a)
      ans=comb(cnt[i],a-(t-cnt[i]))
      break
  ave=ave/a
print(ave)
print(ans)