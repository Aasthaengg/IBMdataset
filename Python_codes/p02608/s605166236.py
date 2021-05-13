N = int(input())
chk = [0] * (10 ** 4 + 2)
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            a = i**2 + j**2 + k**2 + i*j + j*k + i*k
            if a > 10001:
                break
            chk[a] += 1
for i in range(N):
    print(chk[i+1])