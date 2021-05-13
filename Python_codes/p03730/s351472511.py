a, b, c = map(int, input().split())
m = a % b
f = False
for i in range(m):
    f |= ((i % m * b % m + c % m) % m == 0)

print("YES" if f else "NO")
