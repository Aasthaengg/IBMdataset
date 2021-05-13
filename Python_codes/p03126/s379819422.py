N,M=map(int,input().split())
KA=[]
A=[]
a=0
for i in range(N):
    KA.append(list(map(int,input().split())))
for i in range(N):
    KA[i].remove(KA[i][0])
for i in range(N):
    for j in range(len(KA[i])):
        A.append(KA[i][j])
for i in range(1,M+1):
    if N==A.count(i):
        a+=1
print(a)