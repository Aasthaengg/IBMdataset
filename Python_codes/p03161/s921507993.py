n,k=map(int,input().split())
l=list(map(int,input().split()))
final=[0]*n
if k>=n:
  print(abs(l[n-1]-l[0]))
else:   
   for i in range(1,k+1):
      final[i]=abs(l[i]-l[0])
  
   for i in range(k+1,n):

      li=[abs(l[i]-l[ik])+final[ik] for ik in range(i-1,i-k-1,-1) ]
      final[i]=min(li)
   print(final[-1])
