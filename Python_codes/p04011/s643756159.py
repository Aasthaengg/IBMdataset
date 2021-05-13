n = input()
k = input()
x = input()
y = input()

n = int(n)
k = int(k)
x = int(x)
y = int(y)

if n >= k:
    total = k * x + (n - k) * y
else:
    total = n * x
    
print(total)