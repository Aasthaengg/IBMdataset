M, K = map(int, input().split())

if K == 0:
    a  = [i for i in range(2 ** M - 1, -1, -1)]
    a += [i for i in range(2 ** M)]
elif 2 <= M and K < 2 ** M:
    a  = [K] + [i for i in range(2 ** M - 1, -1, -1) if i != K]
    a += [K] + [i for i in range(2 ** M) if i != K]

else:
    a = [-1]

print(' '.join(map(str, a)))
