n = int(input())
a, b = map(int, input().split())
p = [int(i) for i in input().split()]
x = len(list(filter(lambda x: x <= a, p)))
y = len(list(filter(lambda x: a < x <= b, p)))
z = len(list(filter(lambda x: b < x, p)))
print(min(x, y, z))
