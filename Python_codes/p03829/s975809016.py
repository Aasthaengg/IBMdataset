n, a, b = map(int, input().split(' '))
x = list(map(int, input().split(' ')))

t = 0
for i in range(n - 1):
    d = x[i + 1] - x[i]
    t += min(a * d, b)

print(t)