N = int(input())
S = input()
W = []
E = []
w = 0
e = 0
for i in range(N):
    W.append(w)
    if S[i] == 'W':
        w += 1
for j in range(N - 1, -1, -1):
    E.append(e)
    if S[j] == 'E':
        e += 1
R = W[0] + E[N - 1]
for i in range(N):
    R = min(R, W[i] + E[N - 1 - i])
print(R)