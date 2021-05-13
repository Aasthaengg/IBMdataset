a, b = map(int, input().split())

if a == b:
    ans = a + b
else:
    ans = max(a, b) + max(a-1, b -1)

print(ans)