n, m = map(int, input().split())
if n >= 2:
    a = n * (n - 1) / 2
else:
    a = 0
if m >= 2:
    b = m * (m - 1) / 2
else:
    b = 0    
print(int(a + b))