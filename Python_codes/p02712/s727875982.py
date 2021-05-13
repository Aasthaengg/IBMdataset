n = int(input())
c = 0

while n > 0:
    if n % 3 != 0 and n % 5 != 0:
        c += n
    n -= 1

print(c)