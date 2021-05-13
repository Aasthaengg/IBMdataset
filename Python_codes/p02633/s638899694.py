x = int(input())
i = x
count = 1
while True:
    if i % 360 == 0:
        print(count)
        exit()
    i += x
    count += 1