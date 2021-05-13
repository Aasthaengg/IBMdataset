n=int(input())
a=str(input())
b=str(input())
c=str(input())
ans=0

for i in range(n):
  se = set([a[i],b[i],c[i]])
  ans=ans+len(se)-1

print(ans)
