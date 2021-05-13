N,K = map(int, input().split())
H = [int(input()) for i in range(N)]
H.sort()

hold = 0
ans = 10 ** 9 + 1
for i in range(K-1,N):
    hold = H[i] - H[i-(K-1)]
    ans = min(ans, hold)
print(ans)