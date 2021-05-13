n = int(input())
x = input()
count_1 = x.count('1')
value = [0, 0]
x_int = int(x, 2)
value[0] = x_int % (count_1 - 1) if count_1 > 1 else 0
value[1] = x_int % (count_1 + 1)
for i in range(n):
    if x[i] == '0':
        tmp = (pow(2, n - i - 1, count_1 + 1) + value[1]) % (count_1 + 1)
    else:
        if count_1 == 1:
            print(0)
            continue
        tmp = (-pow(2, n - i - 1, count_1 - 1) + value[0]) % (count_1 - 1)
    ans = 1
    while tmp > 0:
        tmp = tmp % (bin(tmp).count('1'))
        ans += 1
    print(ans)