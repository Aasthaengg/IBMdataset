n=int(input())
aM=0
am=10**9
bm=10**9
for _ in range(n):
    a,b = map(int,input().split())
    if a>aM:
        aM=a
        bm=b
    if a<am:
        am=a
ans=aM-am+1
if bm>0:
    ans+=bm
ans+=am-1
print(ans)
