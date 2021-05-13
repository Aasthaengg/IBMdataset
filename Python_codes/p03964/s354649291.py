N = int(input())
TT,AA= map(int,input().split())
for k in range(1,N):
    T,A = map(int,input().split())
    j = max((TT-1+T)//T,(AA-1+A)//A)
    TT = T*j 
    AA = A*j
        
print(TT + AA)