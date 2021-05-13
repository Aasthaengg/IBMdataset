n = int(input())
c = 0

if n % 1000 != 0:
    c = 1000 - n % 1000

print(c)
