X, Y = map(int, input().split())
count = 1
while True:
    X *= 2
    if X <= Y:
        count += 1
    else:
        break
print(count)