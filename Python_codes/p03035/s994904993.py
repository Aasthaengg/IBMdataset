a, b = [int(x) for x in input().split()]
if a < 6:
    b = 0
elif a < 13:
    b //= 2
print(b)