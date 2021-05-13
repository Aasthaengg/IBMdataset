N,K = map(int,input().split())
lsh = list(map(int,input().split()))
ans = 0
for i in range(N):
    if K <= lsh[i]:
        ans += 1
print(ans)