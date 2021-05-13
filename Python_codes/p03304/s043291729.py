n,m,d=map(int,input().split())
t=min(n,d*2)
tt=n-t
if d==0:
    t=n
    tt=0
ans=(m-1)*(tt*2+t)/(n**2)
print(ans)