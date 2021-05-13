N = int(input())
ans = 0
cur = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a > cur:
        ans = a + b
        cur = a
print(ans)