A,B,K=map(int,input().split())
C=[]
for i in range(1,(min(A,B))+1):
    if A%i==0 and B%i==0:
        C.append(i)
C.sort()
print(C[len(C)-K])