s = int(input())

a = [s]
m = 1
while s not in a[:-1]:
    if s % 2 == 0:
        s //= 2
    else:
        s = s * 3 + 1
    a.append(s)
    m += 1 
print(m)
