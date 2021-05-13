A,B,K=map(int, input().split())
for i in range(K):
    if i&1:
        A+=B//2
        B//=2
    else:
        B+=A//2
        A//=2
print(A,B)