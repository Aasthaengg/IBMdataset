N = int(input())
x = list()
u = list()

for a in range(0, N):
    X, U = input().split()
    x.append(float(X))
    u.append(U)

sm = 0

for a, b in zip(x, u):
    if b == 'BTC':
        sm += a*380000
    else:
        sm += a

print(sm)
