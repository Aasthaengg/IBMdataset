

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


x = int(input())
i = x
while True:
    if is_prime(i):
        print(i)
        exit()
    i += 1
