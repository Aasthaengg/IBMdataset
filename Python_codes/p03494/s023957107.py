x = int(input())
y = list(map(int, input().split()))

z = True
count = -1
while z == True:
    count += 1
    for i, j in enumerate(y):
        if j % 2 == 0:
            y[i] = j / 2
        else:
            z = False

print(count)