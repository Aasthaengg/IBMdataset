X,Y=map(int,input().split())
ans=-1
if X%Y==0:
    pass
else:
    for i in range(100):
        if (X*(i+2))%Y!=0:
            ans=X*(i+2)
            break
print(ans)