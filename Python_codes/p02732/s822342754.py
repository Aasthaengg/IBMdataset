import math
def combination(n,r):
    if r<n:
        o=math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    else:
        o=1 if r==n else 0
    return o

N=int(input())
A=list(map(int,input().split()))
l=[0]*N
m=[0]*N
s=0
for i in A:l[i-1]+=1
for i in range(N):
    c=combination(l[i],2)
    s+=c
    m[i]=c-combination(l[i]-1,2)
for i in A:print(s-m[i-1])