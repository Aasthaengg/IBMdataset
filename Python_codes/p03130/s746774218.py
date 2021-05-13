li = []
for _ in range(3):
    li += list(map(int, input().split()))

mx = 0
for i in range(1, 5):
    mx = max(mx, li.count(i))

if mx == 3:
    ans = "NO"
else:
    ans = "YES"

print(ans)
