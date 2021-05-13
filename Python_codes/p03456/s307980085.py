a,b = input().split()
x = 4
ab = int(a+b)
while x*x < ab:
    x += 1
print("Yes" if x*x == ab else "No")