#C
n = int(input())

f = [0 for _ in range(10**5)]

for i in range(1,105):
    for j in range(1,105):
        for k in range(1,105):
            f[i**2 + j**2 + k**2 + i*j + j*k + k*i] += 1

for l in range(n):
    print(f[l+1])