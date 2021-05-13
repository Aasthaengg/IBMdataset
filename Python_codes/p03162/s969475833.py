N = int(input())
a = [0] * N
b = [0] * N
c = [0] * N

for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())

# print(a)
# print(b)
# print(c)
S = [[0 for j in range(3)] for i in range(N)]
S[0][0] = a[0]
S[0][1] = b[0]
S[0][2] = c[0]

for i in range(1, N):
    S[i][0] = max(S[i - 1][1], S[i - 1][2]) + a[i]
    S[i][1] = max(S[i - 1][0], S[i - 1][2]) + b[i]
    S[i][2] = max(S[i - 1][0], S[i - 1][1]) + c[i]

# print(S)
print(max(S[N - 1]))
