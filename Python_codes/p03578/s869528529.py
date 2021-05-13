N=int(input())
*D,=map(int,input().split())
M=int(input())
*T,=map(int,input().split())

from collections import*
d=Counter(D)
t=Counter(T)

print(['NO','YES'][(d&t)==t])