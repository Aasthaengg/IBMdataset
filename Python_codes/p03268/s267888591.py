N, K = list(map(int, input().split()))

ans = int(N/K)**3
if K % 2 == 0:
    ans += (int(N/(K/2))-int(N/K))**3
print(ans)
