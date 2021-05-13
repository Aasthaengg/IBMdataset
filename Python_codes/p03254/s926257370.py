n,x=map(int,input().split())
a=list(map(int, input().split()))

ans=0
rest=x
target=sorted(a)
if sum(target)<x:
    print(n-1)
elif sum(target)==x:
    print(n)
else:
    for i in range(n):
        rest-=target[i]
        if rest<0:
            ans=i
            break
        if rest==0:
            ans=i+1
            break
    print(ans)
