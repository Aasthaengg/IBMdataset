A,B,C=map(int,input().split())
ans=B
if C>A+B:
    ans+=A+B+1
else:
    ans+=C

print(ans)