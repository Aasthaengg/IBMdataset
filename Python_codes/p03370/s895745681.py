N,X = map(int,input().split())
M = [0] * N
for i in range(N):
    M[i] = int(input())
rest = X - sum(M)
min_price = min(M)
print(N + int(rest/min_price))

