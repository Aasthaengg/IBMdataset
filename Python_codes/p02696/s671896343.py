a,b,n=map(int,input().split())
if n>=b:
    x=b-1
    fl1=a*x//b
    fl2=a*(x//b)
else:
    fl1=a*n//b
    fl2=a*(n//b)
    
ans = fl1-fl2
print(ans)