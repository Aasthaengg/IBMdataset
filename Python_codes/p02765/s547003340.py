N, R = list(map(int, input().split()))
if N < 10:
    print(R + 1000 - 100*N)
else:
    print(R)