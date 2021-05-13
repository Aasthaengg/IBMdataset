a, b = [int(x) for x in input().split()]
while b:
    a, b = b, a % b
print(a)