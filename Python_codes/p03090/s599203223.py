N = int(input())

print(N*(N-1)//2-N//2)
for i in range(1, N):
    for j in range(i+1, N+1):
        if N % 2 == 0:
            if i+j != N+1:
                print(i, j)
        else:
            if i+j != N:
                print(i, j)
