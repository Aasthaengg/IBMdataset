N = int(input())
P = list(map(int,input().split()))

cnt = 10**18
ans = 0

for i in range(N):
    if cnt >= P[i]:
        cnt = P[i]
        ans += 1
print(ans)