while True:
    i = list(map(lambda x: int(x), input().split(" ")))
    if i[0] == 0 and i[1] == 0:
        break
    count = 0
    for a in range(1, i[0] - 1):
        for b in range(a+1, i[0]):
            for c in range(b+1, i[0]+1):
                if a + b + c == i[1]:
                    count += 1
    print(count)