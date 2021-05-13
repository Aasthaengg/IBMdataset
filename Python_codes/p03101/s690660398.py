h,w=map(int,input().split())
a,b=map(int,input().split())
ans=((h*w)-(((a*w)+(b*h))-(a*b)))
print(ans)