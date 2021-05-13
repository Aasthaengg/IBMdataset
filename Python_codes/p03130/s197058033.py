a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
lst=[a,b,c,d,e,f]
ans='NO'
if lst.count(1)==1:
  if lst.count(2)==2:
    if lst.count(3)==2:
      if lst.count(4)==1:
        ans='YES'
print(ans)