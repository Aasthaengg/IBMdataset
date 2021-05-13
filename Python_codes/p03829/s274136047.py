N,A,B=map(int,input().split())
now=0
ans=0
for x in map(int,input().split()):
    if now!=0:
        if (x-now)*A>B:
            ans+=B
        else:
            ans+=(x-now)*A
    now=x
print(ans)