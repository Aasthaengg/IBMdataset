N, M = map(int, input().split())

if M//2 < N:
    print(M//2)
elif N < M//2:
    print(N + (M-N*2)//4)