X, Y = map(int, input().split())

a = X
count = 0
while a <= Y:
    count += 1
    a *= 2

print(count)
