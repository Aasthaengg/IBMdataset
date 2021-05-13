a,b,c=map(int,input().split())
m=min(a,b,c)
M=max(a,b,c)
n=a+b+c-m-M
print(M*10+n+m)