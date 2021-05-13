N = int(input())
R = [None] * (N+1)

R[0] = 2
if N == 0:
    print(R[0])
    exit()
R[1] =1
if N == 1:
    print(R[1])
    exit()
if N >= 2:
    for i in range(2, N+1):
        R[i] = R[i-1] + R[i-2]
    print(R[N])