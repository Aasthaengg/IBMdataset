from sys import stdin
data = stdin.read().splitlines()

a = int(data[0])
b = int(data[1])
c = int(data[2])
x = int(data[3])

count = 0

l = min(x//500, a)

while l >= 0:
    x = x - 500*l
    m = min(x//100, b)
    while m >= 0:
        x = x - 100*m
        if c >= x//50:
            count += 1
        x = x + 100*m
        m -= 1
    x = x + 500*l
    l -= 1
print(count)