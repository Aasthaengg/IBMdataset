
n,m = map(int,input().split())

ans,ansf = 1,n

for i in range(m):
    l,r = map(int,input().split())
    ans = max(ans,l)
    ansf = min(ansf,r)
    
if ansf - ans <0:
    print(0)
else:
    print(ansf-ans+1)