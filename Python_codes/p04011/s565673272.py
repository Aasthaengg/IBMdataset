n = int(input())
k = int(input())
x = int(input())
y = int(input())
a = 0
b = 0
c = 0
e = 0

if n <= k:
    a = n * x
else:
    c = n - k
    a = x * k
    b = c * y

e = a + b
print(e)