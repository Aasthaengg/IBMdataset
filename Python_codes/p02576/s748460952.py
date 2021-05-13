N, X, T = map(int,input().split())
C=1
if N%X!=0:
     C=N//X+1
else:
    C=N//X
 
print(C*T)