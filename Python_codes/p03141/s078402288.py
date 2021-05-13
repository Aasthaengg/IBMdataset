n = int(input())
x = []
y = 0
for i in range(n):
    a, b = map(int, input().split())
    y += b
    x.append(a + b)
X = sorted(x)[::-1]
print(sum(X[::2]) - y)
