import math
N = int(input())

jdg = True

for h in range(math.ceil(N/4), 3501):
    for n in range(h, 3501):
        num = 4*h*n - N*h - N*n
        if num > 0:
            if (N * n * h) % num == 0:
                jdg = False
                break
    if not jdg: break

w = N*h*n//(num)
print(*[h, n, w])