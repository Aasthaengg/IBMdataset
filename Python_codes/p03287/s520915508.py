import sys
def input():
    return sys.stdin.readline()[:-1]
N,M=map(int,input().split())
A=list(map(int,input().split()))
l=[None]*N
t=0
for i in range(N):
    t=(A[i]+t)%M
    l[i]=t
l.append(0)
l.sort()
c=0
a=0
t=-1
for i in l:
    if i==t:
        c+=1
    else:
        a+=c*(c-1)//2
        c=1
        t=i
a+=c*(c-1)//2
print(a)