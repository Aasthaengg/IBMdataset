import sys
def input():
    return sys.stdin.readline()[:-1]
N,K=map(int, input().split())
A=tuple(map(int,input().split()))
l=[0]*40
for i in A:
    b=bin(i)
    for i in range(-1,1-len(b),-1):
        if b[i]=="1":
            l[i]+=1
x=[0]*40
xi=0
for i in range(40):
    if l[i]<=N//2 and xi+2**(39-i)<=K:
        x[i]=1
        xi+=2**(39-i)
a=0
for i in range(40):
    if x[i]:
        a+=(N-l[i])*2**(39-i)
    else:
        a+=l[i]*2**(39-i)
print(a)