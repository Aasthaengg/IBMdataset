A,B,K = list(map(int,input().split()))
for i in range(K):
    if i % 2 == 0:
        if A % 2 != 0:
            A -= 1
        A //=2
        B += A
    else:
        if B % 2 != 0:
            B -= 1
        B //=2
        A += B
print(str(A)+' '+str(B))