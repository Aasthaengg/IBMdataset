n1, n2  = [int(i) for i in input().split()]

if n2 % n1 == 0:
    r3 = n1 + n2
else:
    r3 = n2 - n1

print(r3)