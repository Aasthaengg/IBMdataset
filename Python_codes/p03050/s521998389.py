n=int(input())

d=[]
for i in range(1,n):
  if n%i==0:
    d.append(i)
    if i*i!=n:
      d.append(n//i)
  if i*i>=n:
    break

ans=0
for i in d:
  a=i-1
  if a>0:
    if n//a==n%a:
      ans+=a

print(ans)