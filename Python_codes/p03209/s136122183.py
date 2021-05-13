n, x = map(int, input().split())

S, P = [1], [1]
for i in range(n):
    S.append(S[i]*2+3)
    P.append(P[i]*2+1)


def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1+S[n-1]:
        return f(n-1, x-1)
    else:
        return P[n-1] + 1 + f(n-1, x-2-S[n-1])


print(f(n, x))
