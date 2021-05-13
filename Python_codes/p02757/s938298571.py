import collections

n,p=map(int,input().split())
s=input()
arr=[int(s[i]) for i in range(len(s))]
if p==2 or p==5:
  ans=0
  for i in range(n):
    if arr[i]%p==0:
      ans+=i+1
  print(ans)
else:
  dic=collections.defaultdict(int)
  tmp=0
  for i in range(n-1,-1,-1):
    tmp+=arr[i]*pow(10,n-1-i,p)
    tmp%=p
    dic[tmp]+=1
  ans=0
  rem=0
  for i in range(n-1,-1,-1):
    ans+=dic[rem]
    rem+=arr[i]*pow(10,n-1-i,p)
    rem%=p
    dic[rem]-=1
  print(ans)