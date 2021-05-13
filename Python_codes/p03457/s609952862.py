N = int(input())
T = [];X = [];Y = []
for _ in range(N):
    t,x,y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)
if N == 1:
    print('Yes' if T[0] == sum(X+Y) else 'No')
    exit()
for i in range(N):
    if i == 0: continue
    d = abs(X[i] + Y[i] - X[i-1] - Y[i-1])
    t = T[i] - T[i-1]
    if (t + d) % 2 or t < d:
        print('No')
        exit()
else:
    print('Yes')