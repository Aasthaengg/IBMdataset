N, K = map(int,input().split())

ans = 0
cnt = 0
for i in range(K, N+1, K):
    cnt += 1
ans += pow(cnt, 3)

if K % 2 == 0:
    cnt = 0
    for i in range(K//2, N+1, K):
        cnt += 1
    ans += pow(cnt, 3)
print(ans)