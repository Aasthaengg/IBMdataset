a, b, x = [int(x) for x in input().split()]

first = (a // x) * x

if a % x != 0:
    first += x

result = len(range(first, b+1, x))
print(result)
