X, N = map(int,input().split())
P = list(map(int,input().split()))

if N == 0:
    print(X)
    exit()

for i in range(N+1):
    if X - i not in P:
        print(X-i)
        exit()
    elif X + i not in P:
        print(X+i)
        exit()
print(-1)