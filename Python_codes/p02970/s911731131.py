n,d=map(int,input().split())
h=2*d+1
ans=0
while ans*h<n:
    ans+=1
print(ans)