n, k = map(int, input().split())
ans = (n//k)**3
if not k % 2: ans += ((n+k//2)//k)**3
print(ans)
