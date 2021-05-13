n = int(input())
i = 1
l = []
while i <= n:
    x = i
    if x % 3 == 0: l.append(i)
    elif x % 10 == 3: l.append(i)
    else:
        x /= 10
        x = int(x)
        while x:
            if x % 10 == 3:
                l.append(i)
                break
            x /= 10
            x = int(x)
    i += 1
print('',*l)
