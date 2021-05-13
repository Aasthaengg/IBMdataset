N = int(input())

max_num = 3500
for h in range(1,max_num+1):
    for n in range(1, max_num+1):
        if 4*h*n - N*n - N*h <= 0:
            continue
        if N*h*n % (4*h*n - N*n - N*h) == 0:
            w = int(N*h*n / (4*h*n - N*n - N*h))
            Ans = [h, n, w]
            break

print(' '.join(map(str, Ans))) 