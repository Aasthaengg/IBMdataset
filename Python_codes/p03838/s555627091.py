x, y = map(int, input().split())

a = max(0, y - x)
b = max(0, -1 * y - x + 1)
c = max(0, y + x + 1)
d = max(0, -1 * y + x + 2)

l = [a, b, c, d]

ans = 1000000000000

for i in l:
    if i != 0 and i < ans:
        ans = i

print(ans)

