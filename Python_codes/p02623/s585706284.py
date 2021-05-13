n,m,k=map(int,input().split())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
ar=[0]
br=[0]
for i in range(n):
  ar.append(ar[i]+a[i])
for i in range(m):
  br.append(br[i]+b[i])

ans=0
j=0
cnt=0
# print(ar)
# print(br)
for i in range(n+1):
  now=ar[i]
  cnt=i
  nokori=k-now

  if nokori<0:
    continue

  while(br[j]<=nokori):
    if j<m:
      j+=1
    else:
      break
    
  if nokori<br[j]:
    j-=1


  ans=max(ans,j+i)
print(ans)



