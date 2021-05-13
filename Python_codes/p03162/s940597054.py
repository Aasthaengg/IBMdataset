N = int(input())
x, y, z = 0, 0, 0

for i in range(N):
    a, b, c = map(int, input().split())
    x, y, z = a + max(y, z), b + max(x, z), c + max(x, y)
print(max(x, y, z))
