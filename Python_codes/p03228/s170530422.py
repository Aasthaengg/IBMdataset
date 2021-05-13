A,B,K=map(int,input().split())
while True:
    if A%2==1:
        A-=1
    K-=1
    B+=A//2
    A//=2
    if K==0: break
    if B%2==1:
        B-=1
    A+=B//2
    B//=2
    K-=1
    if K==0: break
    
print(A,B)