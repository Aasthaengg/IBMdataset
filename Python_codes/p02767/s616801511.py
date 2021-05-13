import numpy as np

N = int(input())
x_list = list(map(lambda x: int(x), input().split(" ")))
M = np.sum(x_list)
L = np.sum(list(map(lambda x: int(x)**2, x_list)))

if M % N == 0:
    print(int(L - M**2 / N))
else:
    rest = M % N
    if rest <= N / 2:
        print(int(rest**2 / N - M**2 / N + L))
    else:
        print(int(N * (1 - rest / N)**2 - M**2 / N + L))
