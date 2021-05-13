n = int(input())

ans = [0 for _ in range(10005)]

for i in range(1, 105):
    for j in range(1, 105):
        for k in range(1, 105):
            m = i**2 + j**2 + k**2 + i*j + j*k + k*i
            if m < 10005:
                ans[m] += 1

for i in range(n):
    i += 1
    print(ans[i])