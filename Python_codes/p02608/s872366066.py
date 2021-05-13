n = int(input())

l = {}
for i in range(1, n+1):
    l[i] = 0

for x in range(1, min(101, n)):
    for y in range(1, min(101, n)):
        for z in range(1, min(101, n)):
            m = (x + y + z) ** 2 - (x*y + y*z + z*x)
            if m <= n:
                l[m] += 1
for i in range(1, n+1):
    print(l[i])