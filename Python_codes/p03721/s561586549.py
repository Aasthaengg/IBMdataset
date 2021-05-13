n,k=map(int,input().split())
x=[0]*(10**5+1)
for i in range(n):
    a,b=map(int,input().split())
    x[a]+=b
ans=0
for i in range(10**5+1):
    ans+=x[i]
    if ans>=k:
        print(i)
        break
        
