n=int(input())
s,ans,num =1,1,2
for i in range(2, n+1):
  s*=i
l=[]
while s!=1:
  if not s%num:
    l.append(num)
    s//=num
  else:
    num+=1
for i in set(l):
  ans*=l.count(i)+1
  ans%=10**9+7
print(ans%(10**9+7))
