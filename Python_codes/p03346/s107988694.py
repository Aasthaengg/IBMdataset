import sys
def input():
    return sys.stdin.readline()[:-1]
N=int(input())
l=[0]*N
for i in range(N):
    n=int(input())-1
    l[n]=i
a=0
t=1
for i in range(N-1):
    if l[i]<l[i+1]:
        t+=1
    else:
        if a<t:
            a=t
        t=1
if a<t:
    a=t
print(N-a)