N = [int(input()) for i in range(4)]
if N[0] <= N[1]:
    print(N[2] * N[0])
else:
    print(N[2] * N[1] + N[3] * (N[0] - N[1]))