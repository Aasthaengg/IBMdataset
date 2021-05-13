n=int(input())
a=[0]+sorted(list(map(int,input().split())))
for i in range(n):
  if 2*a[i]<a[i+1]:flag=0
  else:flag=1
  a[i+1]+=a[i]
  a[i]*=flag
ans=0
for i in a[::-1]:
  if i:ans+=1
  else:break
print(ans)