N, Y = input().split()
N = int(N)
Y = int(Y)
i = 0
j = 0
k = N - i - j


for i in range(N+1):
    for j in range(N - i + 1):
        k = N - i - j
        SUM = 10000*i + 5000 * j + 1000 * k
        if SUM == Y:
            print(i, j, k)
            exit()
        else:
            continue
        
print('-1', '-1', '-1')