k, s = map(int, input().split())
ans = 0
for i in range(k+1):
    for j in range(max(k+1,min(s-k,k+1))):
        ans += 1 if 0<=s-i-j<=k else 0
print(ans)