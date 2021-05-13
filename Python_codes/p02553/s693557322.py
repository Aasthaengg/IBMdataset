a,b,c,d=map(int,input().split())
res=max(max(a*c,a*d),max(b*c,b*d))
print(res)