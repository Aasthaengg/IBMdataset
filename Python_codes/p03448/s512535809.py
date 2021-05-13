a=int(input())
b=int(input())
c=int(input())
x=int(input())
ans=0
for p in range(a+1):
  for q in range(b+1):
    for r in range(c+1):
      if 500*p+100*q+50*r==x:
        ans+=1
        
print(ans)