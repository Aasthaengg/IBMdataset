N = int(input())
X = [int(x) for x in input().split()]
sum = 0
X.insert(0,0)
X.append(0)

for n in range(N+1):
    sum += abs(X[n] - X[n+1])


for n in range(N):
    l = abs(X[n] - X[n+1])
    r = abs(X[n+1] - X[n+2])

    if X[n] < X[n+1] and X[n+1] < X[n+2]:
        print(sum)
    elif X[n] > X[n+1] and X[n+1] > X[n+2]:
        print(sum)

    elif l < r:
        sep = 2*abs(X[n] - X[n+1])
        print(sum - sep)
    else:
        sep = 2*abs(X[n+2] - X[n+1])
        print(sum - sep)


