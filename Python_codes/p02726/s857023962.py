N, X, Y = map(int, input().split())

ans = [0] * N

for i in range(1,N):
    for j in reversed(range(N+1)):
        if i >= j:
            break

        tmp = min(j-i,abs(X-i)+1+abs(Y-j))
        ans[tmp] += 1

for i in range(1,N):
    print(ans[i])