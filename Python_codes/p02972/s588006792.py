n=int(input())
a=[0]+list(map(int,input().split()))

m=0
ans=[]
c=[0]*(n+1)
for i in reversed(range(1,n+1)):
  if a[i]%2!=c[i]%2:
    m+=1
    ans.append(i)
    j=1
    r=set()
    while j*j<=i:
      if i%j==0:
        r.add(j)
        r.add(i//j)
      j+=1
    for j in r:
      c[j]+=1
      c[j]%=2
        
print(m)
print(*sorted(ans))       