# coding: utf-8
# Your code here!
N=int(input())

l=[0]*2*10**5#ペアを作れるか診断
k=[0]*2*10**5#ansを記録

ans=1
pre=-1
for _ in range(N):
    c=int(input())-1
    if pre==c:
        continue
    l[c]+=1
    ans+=k[c]*min(l[c]-1,1)
    k[c]=ans
    pre=c
    """
    print(c+1)
    print(l[:5],k[:5])
    print(ans)
    """
print(ans%(10**9+7))
