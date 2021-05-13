k,x=map(int,input().split())
for i in range(k*2-1):
  if(i==k*2-2):
    print((x-(k-1))+i)
  else:
    print((x-(k-1))+i,end=(" "))