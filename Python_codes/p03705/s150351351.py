n,a,b=map(int,input().split())
ma=b*(n-1)+a
mi=a*(n-1)+b
print(ma-mi+1 if ma-mi+1>0 else 0)