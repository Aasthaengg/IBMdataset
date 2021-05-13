import sys
def input():
    return sys.stdin.readline()[:-1]
N=int(input())
a=-1
t=-1
for i in range(N):
    A=int(input())
    if t+1<A:
        a=-1
        break
    if t+1==A:
        a+=1
    else:
        a+=A
    t=A
print(a)