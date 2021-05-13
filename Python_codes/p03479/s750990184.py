X, Y = [int(x) for x in input().split()]
pow = 1
for i in range(100):
    if pow > Y // X: break
    pow *= 2

print(i)