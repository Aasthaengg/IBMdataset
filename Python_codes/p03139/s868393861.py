n,a,b=map(int,input().split())
if n>=(a+b):
    ans1=min(a,b)
    ans2=0
else:
    ans1=min(a,b)
    ans2=(a+b)-n
print(ans1,ans2)