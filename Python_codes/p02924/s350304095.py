N=int(input())
if N==1:
  print(0)
  exit(0)
#a=[i for i in range(1,N)]
#print(sum(a))
if (N-1)%2==0:
  print(N*((N-1)//2))
else:
  print(N*((N-1)//2)+((N-1)//2)+1)