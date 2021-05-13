import sys
 
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline()

N =ni()
A=na()
ma = max(A)
ma_in = A.index(ma)
mi = min(A)
mi_in = A.index(mi)
P=[]
if(ma==mi):
    pass
elif(ma<=0):
    for i in reversed(range(1,N)):
        P.append([i+1,i])
elif(mi>=0):
    for i in range(1,N):
        P.append([i,i+1])
else:
    if(abs(ma)>=abs(mi)):
        for i in range(N):
            if(A[i]<0):
                A[i]+=ma
                P.append([ma_in+1,i+1])
        for i in range(1,N):
            P.append([i,i+1])
            #A[i+1]+=A[i]
    elif(abs(ma)<=abs(mi)):
        for i in range(N):
            if(A[i]>0):
                A[i]+=mi
                P.append([mi_in+1,i+1])
        for i in reversed(range(1,N)):
            P.append([i+1,i])
print(len(P))
for p in P:
    print(p[0],p[1])