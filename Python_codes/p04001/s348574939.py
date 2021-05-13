a = [int(x) for x in input()]
n = len(a)

sum_val = 0
for i in range(1 << (n - 1)):
    tmp_val = a[0]
    for j in range(n - 1):
        if (i >> j) & 1:
            sum_val += tmp_val
            tmp_val = a[j + 1]
        else:
            tmp_val = tmp_val * 10 + a[j + 1]
    sum_val += tmp_val
print(sum_val)