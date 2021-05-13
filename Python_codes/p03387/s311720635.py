a=list(map(int,input().split()))
a=sorted(a)

dist1=a[2]-a[0]
dist2=a[2]-a[1]

if (dist1%2)==0 and (dist2%2)==0:
  ans=(dist1+dist2)//2
  print(ans)
  
elif (dist1%2)==1 and (dist2%2)==1:
  ans=(dist1+dist2)//2
  print(ans)
  
elif (dist1%2)==0 and (dist2%2)==1:
  ans=(dist1//2)+(dist2+1)//2
  print(ans+1)
  
else:
  ans=(dist2//2)+(dist1+1)//2
  print(ans+1)