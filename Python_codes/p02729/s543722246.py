N, M = map(int, input().split())
 
g = 0 if N < 2 else (N * (N - 1)) / 2
k = 0 if M < 2 else (M * (M - 1)) / 2
 
print(int(g + k))