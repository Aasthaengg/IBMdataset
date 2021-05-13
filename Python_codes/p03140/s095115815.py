import collections
def func(a,b,c):
    g=0
    l=[a,b,c]
    d=collections.Counter(l)
    x=len(d)
    if x==3:
        g=2
    elif x==2:
        g=1
    return g
N=int(input())
A=input()
B=input()
C=input()
count=0
for i in range(N):
    count+=func(A[i],B[i],C[i])
print(count)
