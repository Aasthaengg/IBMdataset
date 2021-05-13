X,K,D=map(int, input().split())
X=abs(X)
if X-K*D>0:
  print(X-K*D)
else:
  if K%2==0:
    s=X-2*D*int(X/(2*D))
    t=-(s-2*D)
    print(min(abs(s),t))
    
  else:
    s=X-2*D*int((X-D)/(2*D))-D
    t=-(s-2*D)
    
    print(min(abs(s),t))
