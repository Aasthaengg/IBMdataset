A, B, K = map(int, input().split())
for i in range(0, K):
    if(i & 1):
        if(B & 1):
            B -= 1
        A += B//2
        B //= 2
    else:
        if(A & 1):
            A -= 1
        B += A//2
        A //= 2
print("{0} {1}".format(A, B))