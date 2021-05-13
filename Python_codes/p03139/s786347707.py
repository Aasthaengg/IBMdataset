n,a,b=map(int,input().split())
ans1=min(a,b)
if a+b>n:
    ans2=a+b-n
else:
    ans2=0
print(ans1,ans2)
