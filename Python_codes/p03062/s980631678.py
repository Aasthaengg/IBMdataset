n=int(input())
a=list(map(int,input().split()))

a.sort()
s=sum(a)
ans=[]
ans.append(s)
N=n//2

for i in range(1,N+1):
  x=i*2-1
  y=i*2
  s+=a[x-1]*-2
  s+=a[y-1]*-2
  ans.append(s)
  
print(max(ans))
