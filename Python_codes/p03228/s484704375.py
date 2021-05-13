A, B, K = map(int, input().split())

for i in range(K):
    if(i%2 == 0):
        if(A%2 != 0):
            A = (A-1)//2
            B = A+B
        else:
            A = A//2
            B += A
    else:
        if(B%2 != 0):
            B = (B-1)//2
            A += B
        else:
            B = B//2
            A += B
print(A, end=' ')
print(B)