def com_div(x, y):
    dv = []
    m = min(x, y)
    for i in range(1, m + 1):
        if x % i == 0 and y % i == 0:
            dv.append(i)
    dv.sort()
    return dv[::-1]


a, b, k = list(map(int, input().split()))
print(com_div(a, b)[k - 1])