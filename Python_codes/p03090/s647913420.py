N = int(input())

print(N*(N-1)//2-N//2)
if N%2 == 1:
    for i in range(1, N):
        for j in range(i+1, N+1):
            if i == N-j:
                continue
            print(i, j)
else:
    for i in range(2, N):
        print(1, i)
        print(N, i)
    for i in range(2, N):
        for j in range(i+1, N):
            if i+j == N+1:
                continue
            print(i, j)