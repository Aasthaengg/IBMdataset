x = int(input())
a = x
while True:
    isPrime = True
    for i in range(2, x-1):
        if x % i == 0:
            isPrime = False
            break
    if isPrime:
        break
    x += 1
print(x)
