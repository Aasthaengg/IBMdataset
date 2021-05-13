N = int(input())
S = list(input())
e = [0]*(N+1)
w = [0]*(N+1)
if S[0] == 'E':
    e[0] += 1
else:
    w[0] += 1
for i in range(1, N):
    if S[i] == 'E':
        e[i] += e[i-1] + 1
        w[i] += w[i-1]
    else:
        e[i] += e[i-1]
        w[i] += w[i-1] + 1
        
ans = float('inf')
for i in range(N):
    tmp = w[i-1] + e[N-1] - e[i]
    ans = min(ans, tmp)
print(ans)