n,m=map(int,input().split())
a=[int(x) for x in input().split()]
a.sort(reverse=True)
border=sum(a)/(4*m)
ans='Yes'
for i in range(m):
  if a[i]<border:
    ans='No'
    break
print(ans)