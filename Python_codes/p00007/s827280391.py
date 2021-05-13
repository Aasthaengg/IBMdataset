x = int(input())

n = 100000
while x > 0:
    n *= 1.05
    mod = n % 1000
    if mod:
        n += 1000 - mod
    x -= 1

print(int(n))