n=int(input())
a=list(map(int,input().split()))

for i in range(n):
  a[i]-=(i+1)
  
a.sort()

if n%2==0:
  tmp=(a[n//2]+a[n//2-1])//2
else:
  tmp=(a[n//2])
  
ans=0
for aa in a:
  ans+=abs(aa-tmp)
#print(tmp)
#print(a)
print(ans)

  
  

