n,a,b=map(int,input().split())

s=min(a,b)
t=max(a,b)

if s+t<=n:
    u=0

else:
    u=s+t-n

print(str(s)+' '+str(u))