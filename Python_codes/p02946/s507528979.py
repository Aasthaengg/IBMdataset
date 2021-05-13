inp=list(map(int,input().split()))
k=inp[0]
x=inp[1]
a=max(x-k+1,-1*pow(10,6))
b=min(x+k-1,pow(10,6))
for i in range(a,b+1):
  print (i,end=" ")