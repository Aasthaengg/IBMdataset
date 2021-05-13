N = int(input())
S = input()


W = [[] for _ in range(N)]
E = [[] for _ in range(N)]

prev_w = 0
prev_e = 0
for i, s in enumerate(S):
    if s == 'W':
        W[i] = prev_w + 1
    else:
        W[i] = prev_w
    prev_w = W[i]

for i, s in enumerate(S[::-1]):
    if s == 'E':
        E[-i] = prev_e + 1
    else:
        E[-i] = prev_e
    prev_e = E[-i]
        
ans = len(S)
for i in range(N):
    if i == 0:
        cost = E[i+1]
    elif i == N-1:
        cost = W[i-1]
    else:
        cost = W[i-1] + E[i+1]
    ans = min([cost, ans])
print(ans)