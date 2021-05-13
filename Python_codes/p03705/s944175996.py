n,a,b=map(int,input().split())
if (n==1 and a!=b) or a>b:exit(print(0))
mi=b+(n-1)*a
ma=a+(n-1)*b
print(ma-mi+1)
