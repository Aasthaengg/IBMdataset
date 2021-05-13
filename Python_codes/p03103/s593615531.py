n,m=map(int,input().split())
ablist=[]
for i in range(n):
  ab=list(map(int,input().split()))
  ablist.append(ab)
ablistsort=sorted(ablist)
ans=0
ko=0
for i in range(n):
  ans+=ablistsort[i][0]*ablistsort[i][1]
  ko+=ablistsort[i][1]
  if ko>m:
      ans-=(ablistsort[i][0]*ablistsort[i][1])
      ko-=ablistsort[i][1]
      while ko<m:
        ans+=ablistsort[i][0]
        ko+=1
print(ans)