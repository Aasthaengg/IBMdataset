def actual(x, a, b):
    return (x - a) % b


x = int(input())
a = int(input())
b = int(input())

print(actual(x, a, b))