n = input()

a = input()
temp = a
b = input()
temp = b if b < temp else temp
for _ in xrange(n-2):
    now = input()
    if (b - a) < (now - temp):
        a, b = temp, now
    if now < temp:
        temp = now
    elif now > b:
        b = now
print b - a