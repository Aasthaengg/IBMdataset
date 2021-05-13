N, X, Y = map(int, input().split())

ans = [0]*(N-1)
for i in range(N-1):
    for j in range(i+1,N):
        d = min(j-i, abs(X-1-i)+abs(Y-1-j)+1)
        ans[d-1] += 1

for a in ans:
    print(a)