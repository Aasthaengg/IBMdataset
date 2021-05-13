a, b, c = [int(x) for x in input().split()]
d = 0
while a != b + 1 :
    if c % a == 0 : d += 1
    a += 1
print(d)
