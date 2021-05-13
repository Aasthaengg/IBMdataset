n,x,t=map(int,input().split())
print(int(t*n/x) if n%x==0 else t*int((1+n/x)))