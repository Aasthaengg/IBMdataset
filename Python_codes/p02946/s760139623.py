K,X=map(int,input().split())
a=X-K+1
b=X+K
while a<b:
  print(a,end=" ")
  a+=1