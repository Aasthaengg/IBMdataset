n = int(input())
k = int(input())
x = int(input())
y = int(input())

x_days = min(n, k)
y_days = n - x_days

print(x * x_days + y * y_days)