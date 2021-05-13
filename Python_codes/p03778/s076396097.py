w,a,b=map(int,input().split())
if a<b:
    dis=b-(a+w)
else:
    dis=a-(b+w)
print(dis if dis>=0 else 0)