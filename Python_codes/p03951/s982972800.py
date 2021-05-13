N = int(input())
S = str(input())
T = str(input())

res = 0
for i in range(N):
    if S[i:] == T[:N-i]:
        res = N-i
        break

print(2 * N - res)