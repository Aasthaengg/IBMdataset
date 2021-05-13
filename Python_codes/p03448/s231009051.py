A = int(input())
B = int(input())
C = int(input())
X = int(input())

c = 0
for i in range(A + 1):
    if 500 * i > X:
        break
    for j in range(B + 1):
        if 500 * i + 100 * j > X:
            break
        K = X - 500 * i - 100 * j
        if K % 50 == 0:
            k = K / 50
            if k <= C:
                c += 1
print(c)
