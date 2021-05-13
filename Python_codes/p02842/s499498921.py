import math
N = int(input())

X = N / 1.08

if X.is_integer():
    print(int(X))
else:
    if math.floor(math.ceil(X) * 1.08) == N:
        print(math.ceil(X))
    else:
        print(':(')