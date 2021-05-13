N = int(input())
A = list(map(str, input().split()))

B = ['_' for _ in range(N)]
if N % 2 == 0:
    for i, a in enumerate(A):
        if i % 2 == 0:
            B[N//2 + i//2] = a
        else:
            B[N//2 - (i+1)//2] = a
else:
    for i, a in enumerate(A):
        if i % 2 == 0:
            B[N//2 - i//2] = a
        else:
            B[N//2 + (i+1)//2] = a

print(' '.join(B))