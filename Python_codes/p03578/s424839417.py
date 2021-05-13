# coding: utf-8
import collections
n=int(input())
D=list(map(int,input().split()))
m=int(input())
T=list(map(int,input().split()))
T_=list(set(T))
c = collections.Counter(D)
c2 = collections.Counter(T)
flg=True
for t in T_:
    #print(c[t], c2[t])
    if c[t] < c2[t]:
        flg=False
if flg:
    print("YES")
else:
    print("NO")