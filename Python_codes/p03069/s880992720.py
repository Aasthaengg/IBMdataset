N = int(input())
S = input()
B = [0 for _ in range(N+1)]
W = [0 for _ in range(N+1)]
for i in range(N):
    B[i+1] = B[i] + (S[i] == '#')
for i in range(N, 0, -1):
    W[i-1] = W[i] + (S[i-1] == '.')
print(min(B[i]+W[i] for i in range(N+1)))