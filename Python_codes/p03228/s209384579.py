a, b, k = map(int,input().split())
switch = 0

for i in range(k):
    if switch == 0:
        if a % 2 == 1:
            a -= 1
        b += a//2
        a = a//2
        switch = 1
    elif switch == 1:
        if b % 2 == 1:
            b -= 1
        a += b//2
        b = b//2
        switch = 0

print(a, b)
