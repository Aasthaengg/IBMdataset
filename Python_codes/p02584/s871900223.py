# coding: utf-8
x, k, d = map(int,input().split())
x=abs(x)
t=x-k*d
if t>=0:
    ans=t
else:
    l=x//d#一番近いところまでの回数
    p=x%d#一番近いところ
    if (k-l)%2==0:
        ans=p
    else:
        ans=min(abs(p+d), abs(p-d))
print(ans)