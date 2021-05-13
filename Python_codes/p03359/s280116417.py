a, b = map(int, input().split())
ans = 0

if a == b or a < b:
    ans += 1

for i in range(1, a):
    ans += 1

print(ans)