k, s = map(int, input().split())
ans = 0
if s <= k:
    ans = (s+2)*(s+1)/2
else:
    for i in range(k+1):
        for j in range(k+1):
            ans = ans + (0 <= s-i-j <= k)

print(int(ans))