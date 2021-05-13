import sys



def cul1(s,i,j):
    if s[i][j]==1: return "."
    else: return "#"

def cul2(s,i,j):
    if s[i][j]==1: return "#"
    else: return "."

a,b=map(int,input().split())
H=20
print(H*2,100)

s=[[0 for j in range(100)] for i in range(H)]
for i in range(a-1):
    k=(i*2//100)*2
    l=(i*2)%100
    s[k][l]=1

for i in range(H):
    d=""
    for j in range(100):
        d+=cul1(s,i,j)
    print(d)


s=[[0 for j in range(100)] for i in range(H)]
for i in range(b-1):
    k=(i*2//100)*2
    l=(i*2)%100
    s[k][l]=1

for i in range(H-1,-1,-1):
    d=""
    for j in range(100):
        d+=cul2(s,i,j)
    print(d)