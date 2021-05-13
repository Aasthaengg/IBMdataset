n, m = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
d = {0:0}
for i in range(1, n + 1):
    min_ = n + 1
    for j in C:
        if i - j in d:
            tmp = d[i - j] + 1
            if tmp < min_:
                min_ = tmp
    d[i] = min_
print(d[n])
