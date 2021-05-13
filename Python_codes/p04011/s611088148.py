n = int(input())
k = int(input())
x = int(input())
y = int(input())

first = min(n, k) * x
second = max(n-k, 0) * y

print(first + second)