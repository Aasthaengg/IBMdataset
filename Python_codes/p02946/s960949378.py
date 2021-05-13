K,X=map(int,input().split())
t1=X-K+1
t2=X+K
for x in range(t1,t2):
  print(x,end="")
  if x != t2-1:
    print(" ",end="")
  else:
    print("")