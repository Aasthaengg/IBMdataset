N, K = map(int, input().split(' '))
R, S, P = map(int, input().split(' '))
T = list(input())

U = []
for t in T:
    if t == 'r':
        u = 'p'
    elif t == 's':
        u = 'r'
    else:
        u = 's'
    U.append(u)

ans = 0
for i in range(N):
    if i >= K and U[i] == U[i - K]:
        U[i] = ''
    else:
        if U[i] == 'r':
            ans += R
        elif U[i] == 's':
            ans += S
        elif U[i] == 'p':
            ans += P

print(ans)
