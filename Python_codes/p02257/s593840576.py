#Prime Numbers ?´???°
c = 0
for i in range(int(input())):
    n = int(input())
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            break
    else:
        c += 1
print(c)