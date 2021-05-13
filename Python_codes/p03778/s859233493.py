w,a,b=map(int,input().split())
a,b=min(a,b),max(a,b)
print(max(b-a-w,0))