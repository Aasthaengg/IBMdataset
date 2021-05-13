a,b,k=map(int,input().split())

if k<=a:
  print(str(a-k)+' '+str(b))
  
else:
  print(str(0)+' '+str(max(0,b-(k-a))))

