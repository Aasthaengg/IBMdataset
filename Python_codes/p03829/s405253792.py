n, a, b = map(int, input().split())
x = [int(i) for i in input().split()]

su = 0
for i in range(n - 1):
    su += a * (x[i + 1] - x[i]) if a * (x[i + 1] - x[i]) < b else b
print(su)
