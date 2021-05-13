ABK = list(map(int,input().split()))
A=ABK[0]
B=ABK[1]
K=ABK[2]
for i in range(K):
    if i%2==0:
        if A%2==0:
            A = A/2
        elif A%2==1:
            A = (A-1)/2
        B = B+A
    if i%2==1:
        if B%2==0:
            B = B/2
        elif B%2==1:
            B = (B-1)/2
        A = A+B
print(int(A),int(B))