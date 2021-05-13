import sys
 
N = int(sys.stdin.readline())
 
# 4*h*n*w = N * (h*n + n*w + w*h)
# (4*h*n - N*n - N*h) * w = N*h*n
# w = N*h*n / (4*h*n - N*n - N*h)
 
for h in range(1, 3501):
    for n in range(1, 3501):
        a = N*h*n
        b = (4*h*n - N*n - N*h) 
        # print(h, n, a, b)
        if b > 0 and a % b == 0:
            w = a // b
            # print(4/N, 1/h + 1/n + 1/w)
            print(h, n, w)
            sys.exit()