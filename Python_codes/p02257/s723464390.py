from math import sqrt
res = 0

def isprime(x) :
    if x == 2 : return 1
    if (x < 2) or (x % 2 == 0) : return 0

    i = 3
    while i <= sqrt(x) :
        if x % i == 0 : return 0
        i = i + 2

    return 1

for mak in range(int(input())) :
    res += isprime(int(input()))
print(res)