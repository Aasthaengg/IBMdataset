a,b = map(int, input().split())

count = 0
total = 1

if total >= b:
    print(count)
else:
    total = a
    count = 1
    if total >= b:
        print(count)
        exit()
    while True:
        total += (a-1)
        count += 1
        if total >= b:
            print(count)
            break
