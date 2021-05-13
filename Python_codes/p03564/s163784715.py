N = int(input())
K = int(input())

MIN = 10**18
for i in range(2**N):
    s = 1
    for j in range(N):
        if ((i >> j) & 1):
            s *= 2
        else:
            s += K
    MIN = min(s,MIN)
print(MIN)