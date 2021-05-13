n=int(input())
a=[int(x) for x in input().split()]

a_i=[]
pl=0
mi=0
mi_cnt=0
pl_cnt=0
for i in range(n):
  a_i.append((a[i]-(i+1)))
  if a[i]-(i+1)<0:
    mi+=a[i]-(i+1)
    mi_cnt+=1
  else:
    pl+=a[i]-(i+1)
    pl_cnt+=1

a_i.sort()
if n%2==0:
  k=a_i[n//2-1]
  k1=a_i[n//2]
  k=(k+k1)//2
else:
  k=a_i[n//2]

ans=0
for i in a_i:
  ans+=abs(i-k)
print(ans)
