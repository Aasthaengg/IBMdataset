n,a,b=map(int,input().split())
mx=min(a,b)
mn=max(mx-(n-max(a,b)),0)
print(str(mx)+" "+str(mn))
