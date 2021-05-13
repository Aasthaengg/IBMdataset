x = int(input())
while True:
    i = 2
    prime = True
    while i * i <= x:
        if x % i == 0:
            prime = False
            break
        i += 1
    if prime:
        print(x)
        quit()
    x += 1