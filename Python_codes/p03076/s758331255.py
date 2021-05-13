import math


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


l = [int(input()) for _ in range(5)]
ll = [roundup(v) for v in l]

m = sum(ll)
print(min([m - ll[i] + l[i] for i in range(5)]))
