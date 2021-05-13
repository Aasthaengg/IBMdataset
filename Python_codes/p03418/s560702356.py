import sys
def input():
    return sys.stdin.readline()[:-1]
n,k=map(int,input().split())
tmp=0
ans=0
# if k==0:
#     print(n*n)
#     quit()
for i in range(k,n):
    tmp=n//(i+1)
    ans+=(i+1-k)*tmp
    tmp=max(1,k)
    if n%(i+1)-tmp+1>0:
        ans+=n%(i+1)-tmp+1
print(ans)