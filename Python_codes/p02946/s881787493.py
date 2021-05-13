k,x=map(int,input().split())
for i in range(x-k+1,x+k):
  if i != x+k-1:
    print(i,end=' ')
  else:
    print(i,end='')