n = int(input())

m = pow(10, 12)

for i in range(1, n+1):
    if n % i == 0:
        m = min(m, i + n // i - 2)
    
    if i * i > n:
        break

print(m)

