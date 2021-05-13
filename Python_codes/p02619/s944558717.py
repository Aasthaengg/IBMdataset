import numpy as np

D=int(input())
C=np.array(list(map(int,input().split())))
S=[]
for _ in range(D):
    S.append(list(map(int,input().split())))
T=[int(input()) for _ in range(D)]

def last(d):
    l=np.zeros(26,int)
    for i in range(d):
        l[T[i]-1]=i+1
    return l

def decrease(d):
    return np.dot(C,(d-last(d)))



manzoku=0
res=[]
for i in range(D):
    manzoku+=S[i][T[i]-1]
    manzoku-=decrease(i+1)
    res.append(manzoku)

for x in res:
    print(x)