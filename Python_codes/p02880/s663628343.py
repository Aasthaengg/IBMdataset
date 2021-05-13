N = int(input())

for i in range(1, 9 + 1, ):
    q, mod = divmod(N, i)
    if q <= 9 and mod == 0:
        print('Yes')
        exit()

print('No')
