import sys
def input():
    return sys.stdin.readline()[:-1]
N,A,B=map(int,input().split())
X=tuple(map(int,input().split()))
k=B//A
a=0
for i in range(N-1):
    if X[i+1]-X[i]>k:
        a+=B
    else:
        a+=(X[i+1]-X[i])*A
print(a)