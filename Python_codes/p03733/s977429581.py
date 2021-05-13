n,t=map(int,input().split())
l=list(map(int,input().split()))

a=t
for i in range(1,n):
  b=l[i-1]+t
  if l[i]>b:
    a+=t
  else:
    a+=l[i]-l[i-1]
print(a)