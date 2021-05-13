def fctr1(n): 
    f=[]
    c=0
    r=int(n**0.5)
    for i in range(2,r+2):
        while n%i==0:
            c+=1
            n=n//i
        if c!=0:
            f.append([i,c])
            c=0
    if n!=1:
        f.append([n,1])
    return f


n=int(input())
mod=1000000007
ans=1
l=[1 for _ in range(n)]
for i in range(2,n+1):
  f=fctr1(i)
  for x,y in f:
    l[x-1]+=y
for x in l:
  ans*=x
  if ans>=mod:
    ans%=mod

#print(l)
print(ans)