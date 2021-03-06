N = int(input())
S = input()
assert len(S) == N

wr = [0] * (N+1)
bl = [0] * (N+1)

def solve():
    bc = 0
    for i in range(N):
        bl[i] = bc
        if S[i] == '#':
            bc += 1
    bl[N] = bc
    wc = 0
    for i in range(N-1, -1, -1):
        if S[i] == '.':
            wc += 1
        wr[i] = wc
    wr[N] = 0
    minval = N + 100
    mini = None
    for i in range(N+1):
        cost = bl[i] + wr[i]
        if minval > cost:
            minval = cost
            mini = i
    return minval

print(solve())