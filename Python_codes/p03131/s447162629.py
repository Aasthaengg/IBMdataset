k,a,b=map(int,input().split())
if k==1:
    print(2)
    exit()
if b-a<=2:
    print(k+1)
    exit()
if k<=a:
    print(k+1)
    exit()
k-=a-1
ans=a
t=k//2
ans+=(b-a)*t
k-=t*2
ans+=k
print(ans)