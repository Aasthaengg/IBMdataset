n = int(input())

f = [0] * (n+1)

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            s = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if s < n + 1:
                f[s] += 1

for i in range(n):
    print(f[i+1])