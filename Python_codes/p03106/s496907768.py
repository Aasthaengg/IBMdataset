def com_div(x, y):
    dv = []
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            dv.append(i)
    return dv


a, b, k = list(map(int, input().split()))
print(com_div(a, b)[k - 1])
