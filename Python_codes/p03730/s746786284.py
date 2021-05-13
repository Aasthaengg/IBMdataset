A, B, C = map(int, input().split())
s = 0
ans = "NO"

for i in range(100):
    s = B * i + C
    if s % A == 0:
        ans = 'YES'
        break

print(ans)