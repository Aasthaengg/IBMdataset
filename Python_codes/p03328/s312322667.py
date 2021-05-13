a, b = map(int, input().split())
x = b - a
east = 0
for i in range(1, x+1):
    east += i

ans = east - b
print(ans)