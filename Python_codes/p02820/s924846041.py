N, K = [int(s) for s in input().split()]
R, S, P = [int(s) for s in input().split()]
T = input()
own_win = [False] * N


def win(t):
    if t == 'r':
        return P
    elif t == 's':
        return R
    else:
        return S


def janken(i):
    if i >= K:
        if T[i] != T[i - K] or own_win[i - K] is False:
            own_win[i] = True
            return win(T[i])
        else:
            return 0
    else:
        own_win[i] = True
        return win(T[i])


cnt = 0
for i in range(N):
    cnt += janken(i)

print(cnt)