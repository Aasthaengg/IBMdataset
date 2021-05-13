n = int(input())
X = []
for _ in range(n):
    x, l = map(int, input().split())
    X.append((x - l, x + l))

count = 0
current = -1 * float('inf')
for x in sorted(X, key=lambda x: x[1]):
    if x[0] >= current:
        count += 1
        current = x[1]
print(count)