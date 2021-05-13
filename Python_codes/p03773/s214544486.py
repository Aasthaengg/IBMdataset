a,b=map(int,input().split())
ans=a+b
if ans>=24:
    print(ans%24)
else:
    print(ans)