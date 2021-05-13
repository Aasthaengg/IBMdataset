A=[list(map(int,input().split())) for i in range(3)]
N=int(input())
B=[int(input()) for i in range(N)]
num=0
for s in range(3):
    num1=0
    for t in range(3):
        if A[s][t] in B:
            num1+=1
    if num1==3:
        num+=1
for a in range(3):
    num4=0
    for b in range(3):
        if A[b][a] in B:
            num4+=1
    if num4==3:
        num+=1
num2=0
for u in range(3):
    if A[u][u] in B:
        num2+=1
if num2==3:
    num+=1
num3=0
for v in range(3):
    if A[2-v][v] in B:
        num3+=1
if num3==3:
    num+=1
if num>0:
    print('Yes')
else:
    print('No')
