N = int(input())
S = input()
w = [0] * (N+1)
e = [0] * (N+1)
for i in range(N):
    if S[i] == 'W':
        w[i+1] = w[i] + 1
        e[i+1] = e[i]
    if S[i] == 'E':
        e[i+1] = e[i] + 1
        w[i+1] = w[i]
ans = 10 ** 6
for i in range(N):
    ans = min(ans, w[i] + e[N] - e[i + 1])
print(ans)