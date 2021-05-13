A,B,K=map(int,input().split())
def cookie(A,B):
    if A%2==1:
        A-=1
    B+=A//2
    A=A//2
    return A,B
for i in range(K//2):
    A,B=cookie(A,B)
    B,A=cookie(B,A)
if K%2==1:
    A,B=cookie(A,B)
print(A,B)