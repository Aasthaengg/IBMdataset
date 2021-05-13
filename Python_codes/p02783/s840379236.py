n1, n2 = [int(i) for i in input().split()]

r1 = n1 // n2
if n1 % n2 != 0:
    r1 += 1

print(r1)