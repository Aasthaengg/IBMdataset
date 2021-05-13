N=int(input())
T0,X0,Y0=0,0,0
for i in range(N):
  T,X,Y=map(int,input().split())
  tmp=T-T0
  if abs(X-X0)+abs(Y-Y0)>tmp:
    print('No')
    exit()
  else:
    Par=tmp%2
    if Par==1:
      if (abs(X-X0)+abs(Y-Y0))%2==0:
        print('No')
        exit()        
    else:
      if (abs(X-X0)+abs(Y-Y0))%2==1:
        print('No')
        exit()
  T0,X0,Y0=T,X,Y
print('Yes')