N, Y = map(int ,input().split())

for i in range(N+1):
    for j in range(N+1):
        c = N - i - j
        if 0<= c <= 2000 and (10000*i + 5000*j + c*1000) == Y:
            print(i,j,c)
            exit()

print('-1 -1 -1')