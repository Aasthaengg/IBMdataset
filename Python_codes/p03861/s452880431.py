a, b, x = [int(_) for _ in input().split()]

count = b//x - a//x

if a%x == 0:
    count += 1

print(count)