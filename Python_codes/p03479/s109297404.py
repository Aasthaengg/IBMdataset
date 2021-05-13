X, Y = map(int, input().split())

count = 0
while X <= Y:
    Y = Y >> 1
    count += 1

print(count)