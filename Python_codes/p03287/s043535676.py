n,m=map(int,input().split())
a=list(map(int,input().split()))
a[0]%=m
for i in range(n-1):
  a[i+1]=((a[i+1]+a[i]) % m)
dict={}
dict[0]=1;ans=0
for i in range(n):
  try:ans+=dict[a[i]]
  except:dict[a[i]]=0
  dict[a[i]]+=1
print(ans)