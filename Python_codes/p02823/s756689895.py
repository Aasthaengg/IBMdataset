n,a,b = map(int,input().split())
d = b-a
if d%2==0:
    ans=d//2
else:
    ans = min((b+a-1)//2,(2*n-a-b+1)//2)
print(ans)