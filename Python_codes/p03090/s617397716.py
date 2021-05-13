N = int(input())
if N & 1:
    print((N-1)**2//2)
    for i in range(N):
        for j in range(i+1, N):
            if i + j == N - 2 and j < N - 1: continue
            print(i+1, j+1)
else:
    print(N*N//2-N)
    for i in range(N):
        for j in range(i+1, N):
            if i + j == N - 1: continue
            print(i+1, j+1)
