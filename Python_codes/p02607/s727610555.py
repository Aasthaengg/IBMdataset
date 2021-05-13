n = int(input())
ans = 0
for i, a in enumerate(map(int, input().split()), 1):
    if i % 2 == 0:
        continue
    if a % 2 == 1:
        ans += 1
print(ans)
