a, b, c = map(int,input().split())
maxim = max(a, b, c)
bottom = a * b * c // maxim
medium = maxim // 2
medium1 = maxim - medium

ans = abs(bottom * (medium - medium1))
print(ans)