import math
N, K = map(int,input().split())
ans = 0
ans += (N//K)**3

if K%2 == 0:
    cnt = 0
    for i in range(1,N+1):
        if i%K == int(K/2):
            cnt += 1
    ans += cnt**3
    #ans += (math.ceil(N/K))**3
print(ans)