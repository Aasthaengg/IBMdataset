K,T=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
a.reverse()
ans=2*a[0]-sum(a)-1
if ans<0:
    ans=0
print(ans)
