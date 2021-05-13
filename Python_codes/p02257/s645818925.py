import math
n = int(input())
n_p = 0
for i in range(n):
    a = int(input())
    if a == 2:
        n_p += 1
        continue
    elif a % 2 == 0:
        continue
    else:
        j = 3
        while j <= math.sqrt(a):
            if a%j == 0:
                break
            j += 2
        else:
            n_p += 1
print(n_p)