import numpy as np
n,c,k=map(int,input().split())
t=list(int(input()) for _ in range(n))
t.sort()
t=np.array(t)
s=0
num=0
while True:
    e=np.searchsorted(t,t[s]+k,side="right")
    if e-s>c:
        s=s+c
    else:
        s=e
    num+=1
    if s>n-1:
        break
print(num)