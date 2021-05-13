a,b,c=map(int,input().split())
ans=2*min(b,c)
b-=ans//2
c-=ans//2
if c:
    ans+=min(a,c)
    c-=min(a,c)
print(ans+int(c>=1)+b)