n,a,b=map(int,input().split())
r=0
for i in range(1,n+1):
  c=sum([int(i) for i in str(i)])
  if a<=c<=b:
    r+=i
print(r)