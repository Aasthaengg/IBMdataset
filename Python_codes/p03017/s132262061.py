N, A, B, C, D = map(int, input().split())
S = list(input())

def solve(E, x, y, G):
    if y != -1:
        E[y-1] = '#'
    dp = [0]*N
    dp[x-1] = 1
    for i in range(2, N):
        if dp[i-2] or dp[i-1]:
            if E[i] == '.':
                dp[i] = 1
    # print(dp)
    return dp[G-1]

if C < D:
    p = solve(S, B, -1, D)
    q = solve(S, A, -1, C)
else:
    bla = 0
    idx = -1
    for i in range(B-2, N):
        if S[i] == '.':
            bla += 1
        else:
            bla = 0
        if bla == 3:
            idx = i
            break
    # print(idx)
    if idx == -1:
        print('No')
        exit()
    else:
        if D - 1 <= idx - 2:
            print('No')
            exit()

    p = solve(S, A, -1, C)
    q = solve(S, B, -1, D)
    # print(p, q)

if p and q:
    print('Yes')
else:
    print('No')