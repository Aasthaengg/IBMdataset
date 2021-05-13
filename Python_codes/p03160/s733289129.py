N = int(input())
h = list(map(int, input().split()))

S = [0] * N
S[0] = 0
S[1] = abs(h[1] - h[0])

for i in range(2, N):
    jump1 = S[i - 1] + abs(h[i] - h[i - 1])
    jump2 = S[i - 2] + abs(h[i] - h[i - 2])
    S[i] = min(jump1, jump2)

# print(S)
print(S[N - 1])
