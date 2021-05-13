n = int(input())
L = [0 for i in range(10**4+1)]
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            r = x**2 + y**2 + z**2 + x*z + x*y + z*y
            if r <= 10000:
                L[r] += 1
for i in range(1, n+1):
    print(L[i])
