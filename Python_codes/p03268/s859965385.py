N, K = map(int, input().split())
tmp = N//K
ans = tmp**3
if not K % 2:
    ans += (N//(K//2)-tmp)**3
print(ans)
