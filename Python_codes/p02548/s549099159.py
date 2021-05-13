import math
N=int(input())
ans=0
for a in range(1,N):#A固定
    ans+=N//a
    if N%a==0:
        ans-=1
print(ans)