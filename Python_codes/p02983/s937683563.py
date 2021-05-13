L, R = [int(i) for i in input().split()]
if R - L < 2019:
    print(min([(i * j) % 2019 for i in range(L, R) for j in range(L + 1, R + 1)]))
else:
    print(min([(i * j) % 2019 for i in range(L, L + 2019) for j in range(L, L + 2019)]))
