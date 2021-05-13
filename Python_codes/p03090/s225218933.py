N = int(input())
X = list(range(1,N+1))
Nsum = sum(X)

n = 2 
while Nsum % n != 0:
    n += 1

group = [[] for i in range(n)]
value = int(Nsum/n)

for i in range(n-1):
    for j in range(N):
        if sum(X[-j-1:]) > value:
            break
    group[i] = X[-j:]
    X = X[:-j]
    ex = value - sum(group[i])
    if ex != 0:
        group[i].append(X.pop(X.index(ex)))

group[-1] = X

LEN = []
LENpr = 0
for i in range(n):
    LEN.append(len(group[i]))
for i in range(n-1):
    LENpr += LEN[i] * sum(LEN[i+1:])

print(LENpr)

for i in range(n-1):
    for j in range(i+1,n):
        for k in range(LEN[i]):
            for l in range(LEN[j]):
                print(group[i][k],group[j][l])

