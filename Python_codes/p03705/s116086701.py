n,a,b=map(int,input().split())
mi=a*(n-1)+b
ma=b*(n-1)+a
print(max(0,ma-mi+1))