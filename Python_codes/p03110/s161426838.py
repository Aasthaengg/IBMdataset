n = int(input())
otoshidama = 0.0
for i in range(n):
    x, u = input().split()
    if u == 'JPY':
        otoshidama += float(x)
    else:
        otoshidama += float(x) * 380000.0
print(otoshidama)
