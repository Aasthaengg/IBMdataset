import math
from collections import Counter

def comb(n,r):
    f=math.factorial
    return f(n)//(f(r)*f(n-r))

N,A,B=list(map(int,input().split()))
v=sorted(list(map(int,input().split())),reverse=True) # 全要素

m=sum(v[:A])/A # 平均値の最大値(A個の場合)

c=Counter(v[:A]) # 大きい方からA個の要素のみ
# この中の最小の要素は，v[A-1]
a=v[A-1]

n=v.count(a) # v内のaの個数
r=c[a] # c内のaの個数

# n個のaの中から，r個を選ぶ方法
ans=comb(n,r)

# n個のaの中から，r個以上min(r+(B-A),n)個以下を選ぶ方法
# ※これはv[0]==v[A]のときのみ
if v[0]==v[A]:
    for i in range(r+1,min(r+(B-A)+1,n+1)):
        ans+=comb(n,i)

print(m)
print(ans)