N,M = map(int,input().split())
X = list(map(int,input().split()))
if N >= M:
    print(0)
    exit(0)
X.sort()
Y = [(X[i+1]-X[i]) for i in range(M-1)]
Y.sort()

print(sum(Y[:M-N]))
