n = int(input())
k = int(input())
x = int(input())
y = int(input())

l = min(k, n)
a = max(0, n - k)
t = l * x + a * y
print(t)