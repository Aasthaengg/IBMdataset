a, b, c, k = map(int, input().split())
ans = a-b
if k%2: ans *= -1
print(ans)