N, C = map(int, input().split())
D, D2 = [], []
for _ in range(N):
    x, v = map(int, input().split())
    D.append((x,v))
    D2.append((C-x,v))
P, S, x0 = [0], [], 0
for x, v in D:
    P.append(P[-1] + v - (x - x0))
    S.append(P[-1] - x)
    x0 = x
T = [0]
for i in range(N):
    T.append(max(T[-1],S[i]))
Q, R, x0 = [0], [0], 0
for i, d in enumerate(reversed(D)):
    x, v = d
    x = C-x
    Q.append(Q[-1]+v-(x-x0))
    R.append(Q[-1]+T[-2-i])
    x0 = x
m1 = max(P+Q+R)
D = list(reversed(D2))
P, S, x0 = [0], [], 0
for x, v in D:
    P.append(P[-1] + v - (x - x0))
    S.append(P[-1] - x)
    x0 = x
T = [0]
for i in range(N):
    T.append(max(T[-1],S[i]))
Q, R, x0 = [0], [0], 0
for i, d in enumerate(reversed(D)):
    x, v = d
    x = C-x
    Q.append(Q[-1]+v-(x-x0))
    R.append(Q[-1]+T[-2-i])
    x0 = x
m2 = max(P+Q+R)
print(max(m1,m2))