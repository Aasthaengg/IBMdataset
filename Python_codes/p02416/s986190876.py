while True:
    n = input()
    if int(n) == 0:
        break
    else:
        sum = 0
        for i in range(len(n)):
            sum += int(n[i])

        print(sum)