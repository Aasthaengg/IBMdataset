a, b = map(int, input().split())
diff = b - a
h = 0

for i in range(diff):
    h += i + 1

ans = h - b

print(ans)