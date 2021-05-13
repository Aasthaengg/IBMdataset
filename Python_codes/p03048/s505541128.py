r, g, b, n = list(map(int, input().split()))

cnt = 0
for i in range(n//r + 1):
    for j in range(n//g + 1):
        nb = (n - (i*r+j*g))

        if (nb >= 0):
            if (nb % b == 0):
                cnt += 1
        else:
            break

print(cnt)