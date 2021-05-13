import math

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if  n % i == 0:
            return False
    return True

num_prime = []
k = 0
while True:
    try:
        n = input()
    except:
        break
    if prime(int(n)):
        if not int(n) in num_prime:
            k += 1
            num_prime.append(int(n))

print(k)