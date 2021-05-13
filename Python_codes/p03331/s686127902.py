n = int(input())
l = [0] * (n // 2)
for i in range(1, n // 2 + 1):
    sum1 = sum([int(d) for d in str(i)])
    sum2 = sum([int(d) for d in str(n - i)])
    l[i - 1] = sum1 + sum2
print(min(l))