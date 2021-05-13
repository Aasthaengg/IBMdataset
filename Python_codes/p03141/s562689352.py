import sys
def input():
    return sys.stdin.readline()[:-1]
N=int(input())
s=[None]*N
for i in range(N):
    A,B=map(int,input().split())
    s[i]=(A+B,A,B)
s.sort(reverse=1)
i=0
t=0
a=0
while i<N:
    if t:
        a-=s[i][2]
    else:
        a+=s[i][1]
    t=not t
    i+=1
print(a)