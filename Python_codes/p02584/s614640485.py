X,K,D=map(int,input().split())
a=abs(X)//D
b=abs(X)-a*D
if K<a:
  print(abs(X)-K*D)
else:
  if (K-a)%2==0:
    print(b)
  else:
    print(min(abs(b-D),abs(b+D)))