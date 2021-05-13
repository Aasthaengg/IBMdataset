N, K = map(int, input().split())
ans = (N//K)**3
if not(K & 1):
    ans += ((N+(K//2))//K)**3
print(ans)
