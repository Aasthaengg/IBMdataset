R,G,B,n = map(int,input().split())

c = 0
for r in range(n // R + 1):
    x = n - r * R
    for g in range(x // G + 1):
        y = x - g * G
        if(y % B == 0):c += 1
print(c)