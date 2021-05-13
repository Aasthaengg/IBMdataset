from sys import *
from itertools import *
n=int(input())
l=[i for i in range(1,10**4)]
t=list(accumulate(l))
for i in range(len(t)):
    if t[i]==n:
        ans=l[0:i+1]
        for i in ans:
            print(i)
        exit()
    if t[i]>n:
        m=t[i]-n
        ans=l[0:i+1]
        ans.remove(m)
        for i in ans:
            print(i)
        exit()