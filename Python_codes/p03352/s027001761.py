x = int(input())
r = 1

for b in range(1, int(x**0.5 + 1)):
    for p in range(2, 11):
        if b**p > x:
            break
        r = max(r, b**p)
        
print(r)