N = int(input())

lt = [0 for _ in range(50)]
rt = [0 for _ in range(50)]

lt[0] = 1
rt[0] = 1
lt[1] = -2
rt[1] = -1

for i in range(2, 50):
    if i % 2 == 0:
        lt[i] = rt[i - 2] + 1
        rt[i] = lt[i] + 2**i - 1
    else:
        rt[i] = lt[i - 2] - 1
        lt[i] = rt[i] - 2**i + 1


res = [0 for _ in range(50)]
while N:
    for i in range(50):
        if lt[i] <= N <= rt[i]:
            res[~i] = 1
            N -= (-2)**i
            break
            
print(int(''.join(map(str, res))))