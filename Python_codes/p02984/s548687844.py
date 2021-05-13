N = int(input())
A = [0] + list(map(int, input().split()))
B = [0 for i in range(N+1)]
for i in range(1, N+1):
    B[1] += int(((-1)**(i-1))*A[i])
for i in range(1, N+1):
    if i == 1:
        print(B[i], end= ' ')
    else:
        B[i] = int(2*(A[i-1] - (1/2)*B[i-1]))
        if i != N:
            print(B[i], end = ' ')
        else:
            print(B[i])
