N = int(input())

Sum = 0

for i in range(1, N + 1):
    n = N // i

    a = (n * ((2 * i) + (n - 1) * i)) // 2

    Sum += a
    #print(a)
print(Sum)