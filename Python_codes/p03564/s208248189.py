n = int(input())
k = int(input())
s = 1

while n > 0:
    if s > k:
        while n > 0:
            s += k
            n -= 1
    else:
        s *= 2
        n -= 1
print(s)