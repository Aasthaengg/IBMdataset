while True:
    x = int(input())
    if x == 0: break
    sum = 0
    while x:
        sum += x%10
        x = x//10
    print(sum)

