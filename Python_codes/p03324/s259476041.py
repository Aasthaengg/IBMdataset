D,N = map(int, input().split())

cnt = 0
for n in range(1, 10 ** 7):
    can, tmp = 0, n
    while tmp % 100 == 0:
        tmp //= 100
        can += 1
    
    if can == D:
        cnt += 1
    
    if cnt == N:
        print(n)
        exit()