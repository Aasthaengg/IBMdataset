n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n >= k:
    nd = n - k
    total = x*k + y*nd
else:
    total = n*x

print(total)