n = int(input())

def make_divisors(n):
    x = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            x += 1
            if i != n // i:
                x += 1
        i += 1
    return x

s = 0

for i in range(1, n+1, 2):
    #print(make_divisors(i))
    if make_divisors(i) == 8:
        s += 1

print(s)