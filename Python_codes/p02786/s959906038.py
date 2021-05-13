n1 = int(input())

n2 = 0
n3 = 1

while n1 != 0:
    n1 = n1 // 2
    n2 += n3
    n3 *= 2

print(n2)