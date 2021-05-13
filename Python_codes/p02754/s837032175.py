N, A, B = map(int, input().split())
M = N // (A + B)

print(A * M + min(N - M * (A + B), A))