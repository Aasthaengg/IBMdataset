N = int(input())
P = []
for i in range(N):
    P.append(int(input()))

check = [0]*(N+1)
for i in range(N):
    X = P[i]
    check[X] = check[X-1]+1
M = max(check)
print(N-M)
