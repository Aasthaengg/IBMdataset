x,y=map(int,input().split())
m=max(x,y)
mm=min(x,y)
print(m+max(m-1,mm))
