n = int(input())
f = [0]*100000005
for i in range(1, 105):
    for j in range(1, 105):
        for k in range(1, 105):
            x = i**2 + j**2 + k**2 + i*j + j*k+ k*i
            f[x] += 1

for i in range(1, n + 1):
    print(f[i])