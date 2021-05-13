a,b=map(int,input().split())
if b==1:print(0)
elif a==b:print(1)
else:
    if (b-1)%(a-1)>0:print((b-1)//(a-1)+1)
    else:print((b-1)//(a-1))